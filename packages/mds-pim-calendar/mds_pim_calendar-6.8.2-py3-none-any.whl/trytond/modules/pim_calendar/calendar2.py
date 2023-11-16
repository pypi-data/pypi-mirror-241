# -*- coding: utf-8 -*-
# This file is part of the pim_calendar module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

# one or more calendar per Tryton user
# contains events
# can be visible/editable to owner/selected user/group/world (by permission)


from trytond.model import ModelView, ModelSQL, fields, Unique
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.pyson import Eval, Or, Id
from trytond.model import ValueMixin
from trytond.i18n import gettext
from trytond.exceptions import UserError
import icalendar
import pytz
from datetime import datetime, timedelta
from .model import CalendarMultiValueMixin, CalendarValueMixin
from .const import sel_color


# multi value fields
cal_visible = fields.Boolean(
    string='Visible', help="turns the calendar visible or invisible")
cal_color = fields.Selection(
    string='Color', selection=sel_color,
    help="Background color of the calendar events.")
cal_limittext = fields.Boolean(
    string='Limit text length',
    help="avoids empty events in the calendar view by " +
    "shortening the visible text")
cal_limitanz = fields.Integer(
    string='Number of characters',
    help="Number of characters for text length limitation",
    states={'required': Eval('cal_limittext', False)})


class CalendarSettings(CalendarValueMixin, ModelSQL, ValueMixin):
    'User specific settings per calendar'
    __name__ = 'pim_calendar.calendar_setting'

    cal_visible = cal_visible
    cal_color = cal_color
    cal_limittext = cal_limittext
    cal_limitanz = cal_limitanz

    @classmethod
    def default_cal_color(cls):
        """ get 'blue light 2'
        """
        return '#5e8ac7'

    @classmethod
    def default_cal_limittext(cls):
        """ shorten visible text
        """
        return False

    @classmethod
    def default_cal_limitanz(cls):
        """ number of chars
        """
        return 21

    @classmethod
    def default_cal_visible(cls):
        """ new calendars are visible
        """
        return True

    @classmethod
    def add_cal_settings(cls, vlist):
        """ add calendar-settings for user + calendar
            vlist: [(id_user, id_calendar), ...]
        """
        pool = Pool()
        CalendarSettings = pool.get('pim_calendar.calendar_setting')

        to_create = []
        for val1 in vlist:
            (id_user, id_calendar) = val1
            if CalendarSettings.search_count([
                    ('calendar.id', '=', id_calendar),
                    ('iduser.id', '=', id_user)]) == 0:
                to_create.append({
                    'cal_visible': CalendarSettings.default_cal_visible(),
                    'cal_color': CalendarSettings.default_cal_color(),
                    'cal_limittext': CalendarSettings.default_cal_limittext(),
                    'cal_limitanz': CalendarSettings.default_cal_limitanz(),
                    'calendar': id_calendar,
                    'iduser': id_user})

        if to_create:
            CalendarSettings.create(to_create)

# end CalendarSettings


class Calendar(ModelSQL, ModelView, CalendarMultiValueMixin):
    'Calendar'
    __name__ = 'pim_calendar.calendar'

    states_ro = {
        'readonly': ~Or(
            Id('pim_calendar', 'group_calendar_admin').in_(
                Eval('context', {}).get('groups', [])),
            Eval('isowner', False))
    }
    name = fields.Char(
        string=u'Name', help='Title of the calendar',
        required=True, size=30, depends=['isowner'],
        states=states_ro)
    note = fields.Text(string='Note', depends=['isowner'], states=states_ro)
    owner = fields.Many2One(
        string='Owner', help='Owner of the calendar',
        model_name='res.user', required=True, ondelete='CASCADE',
        states={
            'readonly': ~Id('pim_calendar', 'group_calendar_admin').in_(
                Eval('context', {}).get('groups', [])),
        })
    visitors = fields.One2Many(
        string='Visitors',
        help='Users invited to view or edit the calendar',
        model_name='pim_calendar.visitor', field='calendar',
        depends=['isowner'], states=states_ro)
    events = fields.One2Many(
        string='Events', field='calendar',
        model_name='pim_calendar.event', depends=['isowner'],
        states=states_ro)

    # multi value fields - user specific settings
    cal_visible = fields.MultiValue(cal_visible)
    cal_color = fields.MultiValue(cal_color)
    cal_limittext = fields.MultiValue(cal_limittext)
    cal_limitanz = fields.MultiValue(cal_limitanz)

    # views
    isowner = fields.Function(fields.Boolean(
        string='is owner', readonly=True,
        states={'invisible': True}), 'on_change_with_isowner',
        searcher='search_isowner')
    isvisitor = fields.Function(fields.Boolean(
        string='is visitor', readonly=True,
        states={'invisible': True}), 'on_change_with_isvisitor',
        searcher='search_isvisitor')
    name_lim = fields.Function(fields.Char(
        string='Name', readonly=True), 'on_change_with_name_lim')

    @classmethod
    def __setup__(cls):
        super(Calendar, cls).__setup__()
        tab_cal = cls.__table__()
        cls._order.insert(0, ('name', 'ASC'))
        cls._sql_constraints.extend([
            ('cal_uniq',
                Unique(tab_cal, tab_cal.name, tab_cal.owner),
                'pim_calendar.msg_calendar_unique_name'),
            ])
        setattr(cls.cal_visible, 'searcher', 'search_cal_visible')

    @classmethod
    def multivalue_model(cls, field):
        pool = Pool()
        if field in [
                'cal_visible', 'cal_color', 'cal_limittext',
                'cal_limitanz']:
            return pool.get('pim_calendar.calendar_setting')
        return super(Calendar, cls).multivalue_model(field)

    @classmethod
    def default_cal_color(cls, iduser=None, calendar=None, pattern=None):
        """ get 'blue light 2'
        """
        return '#5e8ac7'

    @classmethod
    def default_cal_visible(cls, iduser=None, calendar=None, pattern=None):
        """ new calendars are visible
        """
        return True

    @classmethod
    def default_cal_limittext(cls, iduser=None, calendar=None, pattern=None):
        """ shorten visible text
        """
        return False

    @classmethod
    def default_cal_limitanz(cls, iduser=None, calendar=None, pattern=None):
        """ number of chars
        """
        return 21

    @classmethod
    def search_cal_visible(cls, name, clause):
        """ search in multivalue 'cal_visible'
        """
        pool = Pool()
        CalSetting = pool.get('pim_calendar.calendar_setting')
        ModelData = pool.get('ir.model.data')
        User = pool.get('res.user')

        id_grp = ModelData.get_id('pim_calendar', 'group_calendar_admin')
        id_user = Transaction().user

        qu1 = [('cal_visible', clause[1], clause[2])]

        # if not root or admin - limit to current user
        if (id_user != 0) and \
                (id_grp not in [x.id for x in User(id_user).groups]):
            qu1.append(('iduser', '=', id_user))

        # search in settings, get list of calendars
        res1 = CalSetting.search(qu1)
        return [('id', 'in', [x.calendar.id for x in res1])]

    def get_rec_name(self, name):
        """ create rec_name
        """
        if Transaction().user == self.owner.id:
            return self.name
        else:
            return '%s (%s)' % (self.name, self.owner.rec_name)

    @classmethod
    def search_rec_name(cls, name, clause):
        return [
            'OR',
            ('name',) + tuple(clause[1:]),
            ('owner.name',) + tuple(clause[1:])]

    @fields.depends('name', 'owner', 'cal_limittext', 'cal_limitanz')
    def on_change_with_name_lim(self, name=None):
        maxlen = 21
        name1 = '-'
        owner1 = '-'
        if self.cal_limitanz is not None:
            maxlen = self.cal_limitanz
        if self.name is not None:
            name1 = self.name
        if self.owner:
            owner1 = self.owner.rec_name
            id_owner = self.owner.id
        else:
            id_owner = -1

        if Transaction().user == id_owner:
            t1 = name1
        else:
            t1 = '%s (%s)' % (name1, owner1)

        if (self.cal_limittext is True) and (len(t1) > maxlen):
            if Transaction().user == id_owner:
                t2 = ''
            else:
                t2 = ' (%s)' % owner1
                if len(t2) > 10:
                    t2 = ' (%s*)' % owner1[:6]

            t3 = name1
            if (len(t3) + len(t2)) > maxlen:
                t3 = t3[:maxlen - len(t2) - 1] + '*'

            t1 = '%s%s' % (t3, t2)
        return t1

    def on_change_with_isvisitor(self, name=None):
        """ get True if current user is the owner of the calendar
        """
        Cal2 = Pool().get('pim_calendar.calendar')

        if Cal2.search_count([('isvisitor', '=', True)]):
            return True
        else:
            return False

    @fields.depends('owner')
    def on_change_with_isowner(self, name=None):
        """ get True if current user is the owner of the calendar
        """
        id_user = Transaction().user

        if self.owner:
            if self.owner.id == id_user:
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def search_isvisitor(cls, name, clause):
        """ search in 'isvisitor'
        """
        Event = Pool().get('pim_calendar.event')
        id_user = Transaction().user

        is_owner = [('visitors.visitor.id', '=', id_user)]
        not_owner = [('visitors.visitor.id', '!=', id_user)]
        return Event.get_bool_permclause(clause, is_owner, not_owner)

    @classmethod
    def search_isowner(cls, name, clause):
        """ search in 'isowner'
        """
        Event = Pool().get('pim_calendar.event')
        id_user = Transaction().user

        is_owner = [('owner.id', '=', id_user)]
        not_owner = [('owner.id', '!=', id_user)]
        return Event.get_bool_permclause(clause, is_owner, not_owner)

    @classmethod
    def default_owner(cls):
        """ current user from context
        """
        return Transaction().user

    @classmethod
    def create(cls, vlist):
        """ create calendar, add settings for user
        """
        CalendarSettings = Pool().get('pim_calendar.calendar_setting')

        r1 = super(Calendar, cls).create(vlist)
        CalendarSettings.add_cal_settings([
                (x.owner.id, x.id) for x in r1
            ])
        return r1

    @classmethod
    def write(cls, *args):
        """ write item
        """
        pool = Pool()
        ModelData = pool.get('ir.model.data')
        User = pool.get('res.user')

        id_user = Transaction().user
        id_grp = ModelData.get_id('pim_calendar', 'group_calendar_admin')
        usr_grps = [x.id for x in User(id_user).groups]

        if (id_user != 0) and (id_grp not in usr_grps):
            # user is not root and not admin
            ownfields = ['name', 'note', 'owner', 'visitors', 'events']

            actions = iter(args)
            for items, values in zip(actions, actions):
                # deny write if user is not owner
                for i in items:
                    if id_user != i.owner.id:
                        for k in ownfields:
                            if k in values:
                                raise UserError(gettext(
                                    'pim_calendar.msg_calendar_denyedit_field',
                                    fname=k))
        super(Calendar, cls).write(*args)

    @classmethod
    def ical_data_read(cls, icaldata):
        """ read ical-data from string/binary
        """
        try:
            cal1 = icalendar.Calendar.from_ical(icaldata)
        except Exception as e:
            raise UserError(gettext(
                    'pim_calendar.msg_calendar_importerror',
                    errmsg=str(e)))
        return cal1

    @classmethod
    def ical_data_write(cls, calendar):
        """ export events of the calendar as ical
        """

        def to_utc(dtval):
            tzutc = pytz.timezone('UTC')
            return datetime(
                    dtval.year, dtval.month, dtval.day,
                    dtval.hour, dtval.minute, dtval.second,
                    tzinfo=tzutc)

        cal = icalendar.cal.Calendar()
        cal['prodid'] = '-//m-ds//Tryton module mds-pim_calendar//EN'
        cal['version'] = '1.0'

        tzc = icalendar.Timezone()
        tzc.add('tzid', 'UTC')
        cal.add_component(tzc)

        for i in calendar.events:
            event = icalendar.cal.Event()
            event['summary'] = i.name
            event.add('DESCRIPTION', i.note)
            event.add('uid', '%s-%s' % (calendar.id, i.id))
            if i.wholeday is True:
                event.add('dtstart', i.startday)
                event.add('dtend', i.endday + timedelta(days=1))
            else:
                event.add('dtstart', to_utc(i.startpos))
                event.add('dtend', to_utc(i.endpos))
            event.add('location', i.location)
            if i.create_date is not None:
                event.add('created', to_utc(i.create_date))
            if i.write_date is not None:
                event.add('last-modified', to_utc(i.write_date))
            cal.add_component(event)
        return cal.to_ical()

# Calendar
