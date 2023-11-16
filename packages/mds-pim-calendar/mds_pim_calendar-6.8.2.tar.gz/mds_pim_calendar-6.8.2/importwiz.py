# -*- coding: utf-8 -*-
# This file is part of the pim_calendar module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, fields
from trytond.wizard import Wizard, StateTransition, StateView, Button
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.pyson import Eval
from trytond.i18n import gettext
from trytond.exceptions import UserError


class EventImportWizardStart(ModelView):
    'Import events from ics - start'
    __name__ = 'pim_calendar.wiz_import_event.start'

    icsfile = fields.Binary(
        string="*.ics-File", required=True,
        help='The iCalendar-records in this *.ics-file are ' +
        'imported into the current calendar.')
    calendar = fields.Many2One(
        string="Calendar", readonly=True,
        help="The events are imported into this calendar.",
        model_name='pim_calendar.calendar')

# end EventImportWizardStart


class EventImportWizard(Wizard):
    'Import events from ics'
    __name__ = 'pim_calendar.wiz_import_event'

    start_state = 'start'
    start = StateView(
        model_name='pim_calendar.wiz_import_event.start',
        view='pim_calendar.import_wizard_start_form',
        buttons=[
            Button(string='Cancel', state='end', icon='tryton-cancel'),
            Button(
                string='Import', state='importevents', icon='tryton-save',
                states={
                    'readonly': Eval('icsfile', '').in_([None, ''])})])
    importevents = StateTransition()

    def transition_importevents(self):
        """ import from ics-file
        """
        pool = Pool()
        Calendar = pool.get('pim_calendar.calendar')
        Event = pool.get('pim_calendar.event')

        if self.start.icsfile is None:
            raise UserError(gettext('pim_calendar.msg_wizimp_nofile'))
        elif len(self.start.icsfile) == 0:
            raise UserError(gettext('pim_calendar.msg_wizimp_nofile'))

        ical1 = Calendar.ical_data_read(self.start.icsfile)
        Event.ical_add_events(
            self.start.calendar, [x for x in ical1.walk('VEVENT')])
        return 'end'

    def default_start(self, fields):
        """ fill form
        """
        Calendar = Pool().get('pim_calendar.calendar')
        context = Transaction().context

        if context['active_model'] != 'pim_calendar.calendar':
            raise UserError(gettext(
                'pim_calendar.msg_wizimp_wrongmodel'))

        cal1 = Calendar.browse(context['active_ids'])
        if len(cal1) != 1:
            raise UserError(gettext(
                'pim_calendar.msg_wizimp_onecal'))

        return {'icsfile': '', 'calendar': cal1[0].id}

# end EventImportWizard
