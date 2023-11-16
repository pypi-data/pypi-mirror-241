# -*- coding: utf-8 -*-
# This file is part of the pim_calendar module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool


def create_user(name, login, password):
    User = Pool().get('res.user')

    us1 = User(name=name, login=login, password=password)
    us1.save()
    return us1
# end create_user


def create_calendar(name, owner):
    Calendar = Pool().get('pim_calendar.calendar')

    cal1, = Calendar.create([{
        'name': name,
        'owner': owner,
        'cal_color': Calendar.default_cal_color(),
        'cal_visible': Calendar.default_cal_visible()}])

    return cal1
# end create_calendar
