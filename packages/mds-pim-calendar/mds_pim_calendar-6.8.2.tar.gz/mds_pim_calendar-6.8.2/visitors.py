# -*- coding: utf-8 -*-
# This file is part of the pim_calendar module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

# one or more calendar per Tryton user
# contains events
# can be visible/editable to owner/selected user/group/world (by permission)


from trytond.model import ModelView, ModelSQL, fields, Unique, Index
from trytond.pool import Pool
from trytond.pyson import Id


class Visitor(ModelSQL, ModelView):
    'Visitor'
    __name__ = 'pim_calendar.visitor'

    calendar = fields.Many2One(
        string='Calendar',
        help='Calendar to which the visitor have permissions',
        required=True, ondelete='CASCADE',
        model_name='pim_calendar.calendar')
    visitor = fields.Many2One(
        string='Visitor',
        help='User, who can see or edit the calendar',
        required=True, ondelete='CASCADE', model_name='res.user',
        domain=[
            ['OR',
                ('groups', '=', Id('pim_calendar', 'group_calendar_admin')),
                ('groups', '=', Id('pim_calendar', 'group_calendar_user'))]])
    accchange = fields.Boolean(
        string='Change', help='The user can change existing appointments.')
    acccreate = fields.Boolean(
        string='Create', help='The user can create appointments.')
    accdelete = fields.Boolean(
        string='Delete', help='The user can delete appointments.')

    @classmethod
    def __setup__(cls):
        super(Visitor, cls).__setup__()
        tab_vis = cls.__table__()
        cls._sql_constraints.extend([
            ('uniq_visit',
                Unique(tab_vis, tab_vis.calendar, tab_vis.visitor),
                'pim_calendar.msg_visitor_already_exists')])
        cls._sql_indexes.update({
            Index(
                tab_vis,
                (tab_vis.visitor, Index.Equality())),
            })

    @classmethod
    def default_accchange(cls):
        return False

    @classmethod
    def default_acccreate(cls):
        return False

    @classmethod
    def default_accdelete(cls):
        return False

    def get_rec_name(self, name):
        perms = ['R']
        if self.accchange:
            perms.append('W')
        if self.acccreate:
            perms.append('C')
        if self.accdelete:
            perms.append('D')
        return '%s - %s [%s]' % (
            self.visitor.rec_name or '-',
            self.calendar.rec_name or '-',
            ''.join(perms)
            )

    @classmethod
    def create(cls, vlist):
        """ add settings
        """
        CalendarSettings = Pool().get('pim_calendar.calendar_setting')

        r1 = super(Visitor, cls).create(vlist)

        # add calendar-settings
        CalendarSettings.add_cal_settings([
            (x.visitor.id, x.calendar.id) for x in r1
            ])
        return r1

# end Visitor
