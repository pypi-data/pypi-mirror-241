mds-pim-calendar
================
A Calendar for Tryton.
Supports any number of calendars per Tryton user, sharing calendars
between users with selectable permissions per share.

Install
=======

pip install mds-pim-calendar

Requires
========
- Tryton 6.8
- GooCalendar (>= 0.7)  on client side

Permissions
===========
PIM Calendar defines two new user groups.

* PIM Calendar - User: The user can create their own calendars and share them with other users.
* PIM Calendar - Administrator: The user can view and edit the calendars of all users.


Todo
====
- repeating events
- all-day-events and time-events in a single view, when the Tryton client it supports

Changes
=======

*6.8.2 - 10.11.2023*

- comatibility with Tryton 6.8
