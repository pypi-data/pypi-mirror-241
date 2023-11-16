# -*- coding: utf-8 -*-
# This file is part of the pim_calendar module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.


from trytond.model import ModelView, ModelSQL, fields, Check, Index
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.pyson import Eval, Or, Id
from trytond.exceptions import UserError
from trytond.i18n import gettext
from sql.conditionals import Coalesce
from sql.functions import DateTrunc, DatePart, CurrentDate, Trunc, Extract
from sql import Cast
from datetime import datetime, timedelta
import icalendar


class Event(ModelSQL, ModelView):
    'Event'
    __name__ = 'pim_calendar.event'

    states_ro = {
        'readonly': ~Or(
            Eval('id', -1) < 0,
            Eval('isowner', False),
            Eval('permchange', False),
            Id('pim_calendar', 'group_calendar_admin').in_(
                Eval('context', {}).get('groups', [])))}

    calendar = fields.Many2One(
        string='Calendar', required=True,
        help='Calendar to which the event belongs', ondelete='CASCADE',
        depends=['isowner', 'permchange'],
        model_name='pim_calendar.calendar', states=states_ro)
    name = fields.Char(
        string='Title', required=True, states=states_ro,
        depends=['isowner', 'permchange'])
    location = fields.Char(
        string='Location', states=states_ro, depends=['isowner', 'permchange'])
    note = fields.Text(
        string='Note', states=states_ro, depends=['isowner', 'permchange'])
    startpos = fields.DateTime(
        string='Begin', required=True, states=states_ro,
        depends=['isowner', 'permchange'])
    endpos = fields.DateTime(
        string='End', required=True, states=states_ro,
        depends=['isowner', 'permchange'])
    wholeday = fields.Boolean(string='Whole Day', states=states_ro)

    # permissions for visitors, owner has full access
    isowner = fields.Function(fields.Boolean(
        string='Owner', readonly=True,
        help=u'Permission: full access - for current user'),
        'on_change_with_isowner', searcher='search_isowner')
    isvisitor = fields.Function(fields.Boolean(
        string='Visitor', readonly=True,
        help=u'Permission: read - for current user'),
        'on_change_with_isvisitor', searcher='search_isvisitor')
    permchange = fields.Function(fields.Boolean(
        string='Permission: Change', readonly=True,
        help='Permission: change - for current visitor'),
        'on_change_with_permchange', searcher='search_permchange')
    permcreate = fields.Function(fields.Boolean(
        string='Permission: Create', readonly=True,
        help='Permission: create - for current visitor'),
        'on_change_with_permcreate', searcher='search_permcreate')
    permdelete = fields.Function(fields.Boolean(
        string='Permission: Delete', readonly=True,
        help='Permission: delete - for current visitor'),
        'on_change_with_permdelete', searcher='search_permdelete')

    # views
    dayss = fields.Function(fields.Integer(
        string='Days start', readonly=True),
        'get_days_data', searcher='search_dayss')
    dayse = fields.Function(fields.Integer(
        string='Days end', readonly=True),
        'get_days_data', searcher='search_dayse')
    weeks = fields.Function(fields.Integer(
        string='Weeks', readonly=True),
        'get_days_data', searcher='search_weeks')
    months = fields.Function(fields.Integer(
        string='Months', readonly=True),
        'get_days_data', searcher='search_months')
    years = fields.Function(fields.Integer(
        string='Years', readonly=True),
        'get_days_data', searcher='search_years')
    startday = fields.Function(fields.Date(
        string='Begin', readonly=True),
        'get_days_data', searcher='search_startday')
    endday = fields.Function(fields.Date(
        string='End', readonly=True),
        'get_days_data', searcher='search_endday')

    # colors, texts
    bgcolor = fields.Function(fields.Char(
        string='Color', readonly=True), 'on_change_with_bgcolor')
    location_lim = fields.Function(fields.Char(
        string='Location', readonly=True), 'on_change_with_location_lim')
    name_lim = fields.Function(fields.Char(
        string='Name', readonly=True), 'on_change_with_name_lim')
    calendar_name = fields.Function(fields.Char(
        string='Calendar', readonly=True), 'on_change_with_calendar_name')

    @classmethod
    def __setup__(cls):
        super(Event, cls).__setup__()
        tab_event = cls.__table__()
        cls._order.insert(0, ('name', 'ASC'))
        cls._order.insert(0, ('startpos', 'DESC'))
        cls._sql_constraints.extend([
            ('order_time',
                Check(tab_event, (
                    (tab_event.startpos < tab_event.endpos) &
                    (tab_event.wholeday == False)) | (
                    (tab_event.startpos <= tab_event.endpos) &
                    (tab_event.wholeday == True))),
                'pim_calendar.msg_event_start_end_order'),
            ])
        cls._sql_indexes.update({
            Index(
                tab_event,
                (tab_event.startpos, Index.Range(order='ASC'))),
            Index(
                tab_event,
                (tab_event.endpos, Index.Range(order='ASC'))),
            })

    @classmethod
    def view_attributes(cls):
        return super(Event, cls).view_attributes() + [
            ('//group[@id="startpos1"]', 'states',
                {'invisible': Eval('wholeday', False)}),
            ('//group[@id="startpos2"]', 'states',
                {'invisible': ~Eval('wholeday', False)}),
            ('//group[@id="endpos1"]', 'states',
                {'invisible': Eval('wholeday', False)}),
            ('//group[@id="endpos2"]', 'states',
                {'invisible': ~Eval('wholeday', False)}),
            ]

    @classmethod
    def search_rec_name(cls, name, clause):
        return [('name',) + tuple(clause[1:])]

    def get_rec_name(self, name):
        """ create rec_name
        """
        t1 = '-'
        d1 = '-'
        d2 = '-'
        if self.name is not None:
            t1 = self.name
        if self.startpos is not None:
            d1 = self.startpos.strftime('%d.%m.%Y %H:%M')
        if self.endpos is not None:
            if (self.startpos.year == self.endpos.year) and \
                    (self.startpos.month == self.endpos.month) and \
                    (self.startpos.day == self.endpos.day):
                d2 = self.endpos.strftime('%H:%M')
            else:
                d2 = self.endpos.strftime('%d.%m.%Y %H:%M')
        c1 = '-/-'
        if self.calendar:
            c1 = self.calendar.rec_name
        return '%s - %s - %s (%s)' % (t1, d1, d2, c1)

    @classmethod
    def get_calendarlst(cls):
        """ get default calendars
        """
        pool = Pool()
        Calendar = pool.get('pim_calendar.calendar')
        ModelData = pool.get('ir.model.data')
        trans1 = Transaction()

        id_user = trans1.user
        context = trans1.context

        id_grp = ModelData.get_id('pim_calendar', 'group_calendar_admin')

        if (id_grp in context.get('groups', [])) or \
                (len(context.get('groups', [])) == 0):
            # admin gets all calendars
            c_lst = Calendar.search([], order=[('name', 'ASC')])
        else:
            # find a calendar owned by current user
            c_lst = Calendar.search([
                        ('owner.id', '=', id_user),
                    ], order=[('name', 'ASC')])
            # add calendars with edit/create-permission of other users
            c_lst.extend(Calendar.search([
                ('visitors.visitor.id', '=', id_user),
                ['OR',
                    ('visitors.acccreate', '=', True),
                    ('visitors.accchange', '=', True),
                    ('visitors.accdelete', '=', True)]],
                order=[('name', 'ASC')]))
        return [x.id for x in c_lst]

    @classmethod
    def default_startpos(cls):
        """ set to now
        """
        return datetime.now()

    @classmethod
    def default_endpos(cls):
        """ set to now + 30 min
        """
        return datetime.now() + timedelta(seconds=60 * 30)

    @classmethod
    def default_calendar(cls):
        """ get writable calendar
        """
        cal_lst = cls.get_calendarlst()

        if len(cal_lst) > 0:
            return cal_lst[0]
        else:
            return None

    def limit_textlength(self, text):
        if text is not None:
            if self.calendar:
                if self.calendar.cal_limittext and \
                        (len(text) > self.calendar.cal_limitanz):
                    return text[:self.calendar.cal_limitanz - 1] + '*'

            return text
        else:
            return None

    @classmethod
    def default_wholeday(cls):
        return False

    @fields.depends('id')
    def on_change_with_isowner(self, name=None):
        """ get True if current user is owner
        """
        Evnt2 = Pool().get('pim_calendar.event')

        if Evnt2.search_count([
                ('isowner', '=', True), ('id', '=', self.id)]) == 1:
            return True
        else:
            return False

    @fields.depends('id')
    def on_change_with_permchange(self, name=None):
        """ get True if current user is visitor and
            has change-permission
        """
        Evnt2 = Pool().get('pim_calendar.event')

        if Evnt2.search_count([
                ('permchange', '=', True), ('id', '=', self.id)]) == 1:
            return True
        else:
            return False

    @fields.depends('id')
    def on_change_with_permcreate(self, name=None):
        """ get True if current user is visitor and
            has create-permission
        """
        Evnt2 = Pool().get('pim_calendar.event')

        if Evnt2.search_count([
                ('permcreate', '=', True), ('id', '=', self.id)]) == 1:
            return True
        else:
            return False

    @fields.depends('id')
    def on_change_with_permdelete(self, name=None):
        """ get True if current user is visitor and
            has create-permission
        """
        Evnt2 = Pool().get('pim_calendar.event')

        if Evnt2.search_count([
                ('permdelete', '=', True), ('id', '=', self.id)]) == 1:
            return True
        else:
            return False

    @fields.depends('id')
    def on_change_with_isvisitor(self, name=None):
        """ get True if current user is visitor
        """
        Evnt2 = Pool().get('pim_calendar.event')

        if Evnt2.search_count([
                ('isvisitor', '=', True), ('id', '=', self.id)]) == 1:
            return True
        else:
            return False

    @fields.depends('calendar', '_parent_calendar.name_lim')
    def on_change_with_calendar_name(self, name=None):
        if self.calendar:
            return self.calendar.name_lim
        return None

    @fields.depends(
        'location', 'calendar', '_parent_calendar.cal_limitanz',
        '_parent_calendar.cal_limittext')
    def on_change_with_location_lim(self, name=None):
        return self.limit_textlength(self.location)

    @fields.depends(
        'name', 'calendar', '_parent_calendar.cal_limitanz',
        '_parent_calendar.cal_limittext')
    def on_change_with_name_lim(self, name=None):
        return self.limit_textlength(self.name)

    @fields.depends('calendar', '_parent_calendar.cal_color')
    def on_change_with_bgcolor(self, name=None):
        Calendar = Pool().get('pim_calendar.calendar')

        if self.calendar is None:
            return Calendar.default_cal_color()
        else:
            if self.calendar.cal_color is None:
                return Calendar.default_cal_color()
            return self.calendar.cal_color

    @fields.depends('wholeday', 'startpos', 'endpos')
    def on_change_wholeday(self):
        """ at 'wholeday'=True - set time to 0
        """
        Event = Pool().get('pim_calendar.event')

        if (self.startpos is not None) and \
                (self.endpos is not None) and \
                (self.wholeday is not None):
            if self.wholeday is True:
                self.startpos = Event.setdate_wholeday(self.startpos)
                self.endpos = Event.setdate_wholeday(self.endpos)

    @fields.depends('startpos', 'endpos', 'wholeday')
    def on_change_startpos(self):
        """ update endpos
        """
        if (self.startpos is not None) and \
                (self.endpos is not None):
            if self.startpos >= self.endpos:
                self.endpos = self.startpos + timedelta(seconds=60)
            self.on_change_wholeday()

    @fields.depends('startpos', 'endpos', 'wholeday')
    def on_change_endpos(self):
        """ update startpos
        """
        if (self.startpos is not None) and \
                (self.endpos is not None):
            if self.startpos >= self.endpos:
                if self.wholeday is False:
                    self.startpos = self.endpos - timedelta(seconds=60)
                else:
                    self.startpos = self.endpos
            self.on_change_wholeday()

    @classmethod
    def setdate_wholeday(cls, dtime):
        """ set time of 'datetime' to '0:00:00'
        """
        if dtime is None:
            return None
        return datetime(dtime.year, dtime.month, dtime.day, 0, 0, 0)

    @classmethod
    def get_bool_permclause(cls, clause, is_true, is_false):
        """ check clause, get true/false result
        """
        if clause[1] == '=':
            if bool(clause[2]) is True:
                return is_true
            elif bool(clause[2]) is False:
                return is_false
            else:
                raise ValueError('invalid parameter: %s' % str(clause))
        elif clause[1] == '!=':
            if bool(clause[2]) is False:
                return is_true
            elif bool(clause[2]) is True:
                return is_false
            else:
                raise ValueError('invalid parameter: %s' % str(clause))
        else:
            raise ValueError('invalid parameter: %s' % str(clause))

    @classmethod
    def search_isowner(cls, name, clause):
        """ get owner for current user
        """
        id_user = Transaction().user

        is_owner = [('calendar.owner.id', '=', id_user)]
        not_owner = [('calendar.owner.id', '!=', id_user)]
        return cls.get_bool_permclause(clause, is_owner, not_owner)

    @classmethod
    def search_permchange(cls, name, clause):
        """ get change-permission for current user
        """
        id_user = Transaction().user
        Visitor = Pool().get('pim_calendar.visitor')

        visitor_query = Visitor.search([
            ('accchange', '=', True), ('visitor.id', '=', id_user)],
            query=True)

        has_change = [
            'OR',
            ('calendar.visitors.id', 'in', visitor_query),
            ('calendar.owner.id', '=', id_user)]
        not_change = [
            ('calendar.visitors.id', 'not in', visitor_query),
            ('calendar.owner.id', '!=', id_user)]
        return cls.get_bool_permclause(clause, has_change, not_change)

    @classmethod
    def search_permcreate(cls, name, clause):
        """ get create-permission for current user
        """
        id_user = Transaction().user
        Visitor = Pool().get('pim_calendar.visitor')

        visitor_query = Visitor.search([
            ('acccreate', '=', True), ('visitor.id', '=', id_user)],
            query=True)

        has_change = [
            'OR',
            ('calendar.visitors.id', 'in', visitor_query),
            ('calendar.owner.id', '=', id_user)]
        not_change = [
                ('calendar.visitors.id', 'not in', visitor_query),
                ('calendar.owner.id', '!=', id_user)
            ]
        return cls.get_bool_permclause(clause, has_change, not_change)

    @classmethod
    def search_permdelete(cls, name, clause):
        """ get delete-permission for current user
        """
        id_user = Transaction().user
        Visitor = Pool().get('pim_calendar.visitor')

        visitor_query = Visitor.search([
            ('accdelete', '=', True), ('visitor.id', '=', id_user)],
            query=True)

        has_del = [
            'OR',
            ('calendar.visitors.id', 'in', visitor_query),
            ('calendar.owner.id', '=', id_user)]
        not_del = [
            ('calendar.visitors.id', 'not in', visitor_query),
            ('calendar.owner.id', '!=', id_user)]
        return cls.get_bool_permclause(clause, has_del, not_del)

    @classmethod
    def search_isvisitor(cls, name, clause):
        """ get read-permission for current user if is visitor
        """
        id_user = Transaction().user
        Visitor = Pool().get('pim_calendar.visitor')

        visitor_query = Visitor.search([
            ('visitor.id', '=', id_user)], query=True)

        has_change = [('calendar.visitors.id', 'in', visitor_query)]
        not_change = [('calendar.visitors.id', 'not in', visitor_query)]
        return cls.get_bool_permclause(clause, has_change, not_change)

    @classmethod
    def get_days_data_sql(cls):
        """ sql-code
            days/weeks/month: current = 0, last = 1, ...
        """
        tab_event = cls.__table__()
        q1 = tab_event.select(
            tab_event.id.as_('id_event'),
            Cast(Extract(
                'days', DateTrunc('day', Coalesce(
                    tab_event.startpos, CurrentDate())) -
                CurrentDate()), 'integer').as_('dayss'),    # days-start
            Cast(Extract(
                'days', DateTrunc('day', Coalesce(
                    tab_event.endpos, CurrentDate())) -
                CurrentDate()), 'integer').as_('dayse'),    # days-end
            Cast(Trunc(Extract(
                'days', DateTrunc(
                    'day', Coalesce(
                        tab_event.startpos, CurrentDate())) -
                    CurrentDate()) / 7.0), 'integer').as_('weeks'),
            Cast(DatePart(
                'year',  Coalesce(
                    tab_event.startpos, CurrentDate())) -
                    DatePart('year',  CurrentDate()), 'integer').as_('years'),
            Cast((DatePart(
                'year', Coalesce(tab_event.startpos, CurrentDate())) -
                DatePart('year', CurrentDate())) * 12 +
                (DatePart(
                    'month', Coalesce(tab_event.startpos, CurrentDate())) -
                    DatePart('month', CurrentDate())),
                    'integer').as_('months'),
            Cast(DateTrunc('day', tab_event.startpos), 'date').as_('startday'),
            Cast(DateTrunc('day', tab_event.endpos), 'date').as_('endday'),
            )
        return q1

    @classmethod
    def get_days_data(cls, events, names):
        """ get relative number of day/week/month/year
            cuttent = 0, last = 1, ...
        """
        r1 = {
            'dayss': {}, 'dayse': {},
            'weeks': {}, 'months': {}, 'years': {},
            'startday': {}, 'endday': {}
            }
        cursor = Transaction().connection.cursor()

        sql1 = cls.get_days_data_sql()
        qu2 = sql1.select(
            sql1.id_event,
            sql1.dayss,
            sql1.dayse,
            sql1.weeks,
            sql1.months,
            sql1.years,
            sql1.startday,
            sql1.endday,
            where=sql1.id_event.in_([x.id for x in events]))
        cursor.execute(*qu2)
        l2 = cursor.fetchall()

        for i in l2:
            (id1, ds1, de1, w1, m1, y1, sd1, ed1) = i
            r1['dayss'][id1] = ds1
            r1['dayse'][id1] = de1
            r1['weeks'][id1] = w1
            r1['months'][id1] = m1
            r1['years'][id1] = y1
            r1['startday'][id1] = sd1
            r1['endday'][id1] = ed1

        r2 = {}
        for i in names:
            r2[i] = r1[i]
        return r2

    @classmethod
    def search_startday(cls, name, clause):
        """ search in startday
        """
        sql1 = cls.get_days_data_sql()
        Operator = fields.SQL_OPERATORS[clause[1]]

        qu1 = sql1.select(
            sql1.id_event,
            where=Operator(sql1.startday, clause[2]))
        return [('id', 'in', qu1)]

    @classmethod
    def search_endday(cls, name, clause):
        """ search in endday
        """
        sql1 = cls.get_days_data_sql()
        Operator = fields.SQL_OPERATORS[clause[1]]

        qu1 = sql1.select(
            sql1.id_event,
            where=Operator(sql1.endday, clause[2]))
        return [('id', 'in', qu1)]

    @classmethod
    def search_dayss(cls, name, clause):
        """ search in days-start
        """
        sql1 = cls.get_days_data_sql()
        Operator = fields.SQL_OPERATORS[clause[1]]

        qu1 = sql1.select(
            sql1.id_event,
            where=Operator(sql1.dayss, clause[2]))
        return [('id', 'in', qu1)]

    @classmethod
    def search_dayse(cls, name, clause):
        """ search in days-end
        """
        sql1 = cls.get_days_data_sql()
        Operator = fields.SQL_OPERATORS[clause[1]]

        qu1 = sql1.select(
            sql1.id_event,
            where=Operator(sql1.dayse, clause[2]))
        return [('id', 'in', qu1)]

    @classmethod
    def search_weeks(cls, name, clause):
        """ search in weeks
        """
        sql1 = cls.get_days_data_sql()
        Operator = fields.SQL_OPERATORS[clause[1]]

        qu1 = sql1.select(
            sql1.id_event,
            where=Operator(sql1.weeks, clause[2]))
        return [('id', 'in', qu1)]

    @classmethod
    def search_months(cls, name, clause):
        """ search in months
        """
        sql1 = cls.get_days_data_sql()
        Operator = fields.SQL_OPERATORS[clause[1]]

        qu1 = sql1.select(
            sql1.id_event,
            where=Operator(sql1.months, clause[2]))
        return [('id', 'in', qu1)]

    @classmethod
    def search_years(cls, name, clause):
        """ search in years
        """
        sql1 = cls.get_days_data_sql()
        Operator = fields.SQL_OPERATORS[clause[1]]

        qu1 = sql1.select(
            sql1.id_event,
            where=Operator(sql1.years, clause[2]))
        return [('id', 'in', qu1)]

    @classmethod
    def ical_add_events(cls, calendar, event_lst):
        """ create event in selected calendar from icalendar.Event()
        """
        Event = Pool().get('pim_calendar.event')

        def get_datetime(dtval, fulld):
            if not isinstance(dtval, datetime):
                dtval = datetime(dtval.year, dtval.month, dtval.day, 0, 0, 0)
                fulld = True
            return (dtval, fulld)

        to_create = []
        for evt in event_lst:
            if not isinstance(evt, icalendar.Event):
                raise ValueError(
                    "wrong type of event, expected 'icalendar.Event()', " +
                    "got '%s'" % str(type(evt)))

            r1 = {
                'calendar': calendar.id,
                'name': evt['SUMMARY'],
                'note': evt.get('DESCRIPTION', None),
                }
            fullday = False

            (r1['startpos'], fullday) = get_datetime(
                evt['DTSTART'].dt, fullday)
            if 'DTEND' in evt.keys():
                (r1['endpos'], fullday) = get_datetime(
                    evt['DTEND'].dt, fullday)
            elif 'DURATION' in evt.keys():
                (r1['endpos'], fullday) = get_datetime(
                    evt['DTSTART'].dt + evt['DURATION'].dt, fullday)
            else:
                raise UserError(gettext(
                    'pim_calendar.msg_event_import_noend',
                    evttxt=evt['SUMMARY']))

            # if whole-day=true: endpos is at next day
            # we store this at same day and mark the event as 'wholeday=True'
            if (fullday is True) and (
                    r1['endpos'] >= (r1['startpos'] + timedelta(days=1))):
                r1['endpos'] = r1['endpos'] - timedelta(days=1)
            r1['wholeday'] = fullday
            to_create.append(r1)
        if to_create:
            return Event.create(to_create)
        return []

    @classmethod
    def create(cls, vlist):
        """ create item
        """
        vlist = [x.copy() for x in vlist]
        for values in vlist:

            if 'wholeday' in values:
                if values['wholeday'] is True:
                    if 'startpos' in values:
                        values['startpos'] = cls.setdate_wholeday(
                            values['startpos'])
                    if 'endpos' in values:
                        values['endpos'] = cls.setdate_wholeday(
                            values['endpos'])
        return super(Event, cls).create(vlist)

    @classmethod
    def write(cls, *args):
        """ write item
        """
        actions = iter(args)
        for items, values in zip(actions, actions):

            if 'wholeday' in values:
                if values['wholeday'] is True:
                    if 'startpos' in values:
                        values['startpos'] = cls.setdate_wholeday(
                            values['startpos'])
                    if 'endpos' in values:
                        values['endpos'] = cls.setdate_wholeday(
                            values['endpos'])

        super(Event, cls).write(*args)

# end Event
