# -*- coding: utf-8 -*-
# This file is part of the pim_calendar module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase

from .calendar import CalendarTestCase
from .visitor import VisitorsTestCase
from .events import EventsTestCase
from .importwiz import ImportWizardTestCase


class CalendarModuleTestCase(
            CalendarTestCase,
            EventsTestCase,
            VisitorsTestCase,
            ImportWizardTestCase,
            ModuleTestCase):
    'Test calendar module'
    module = 'pim_calendar'

# end CalendarModuleTestCase


del ModuleTestCase
