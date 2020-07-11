#!/usr/bin/env python
# encoding: utf-8
# Created by Keeson <coolkeeson@Hotmail.com> at 2019-05-09    
"""
   Desc:
"""

import datetime

DATE_FORMAT = "%Y-%m-%d"

WEEKDAY_DICT = {
    1: '一',
    2: '二',
    3: '三',
    4: '四',
    5: '五',
    6: '六',
    7: '日'
}


def today():
    return datetime.datetime.today().strftime(DATE_FORMAT)


def add_day(day, delta):
    d1 = datetime.datetime.strptime(day, DATE_FORMAT)
    d2 = d1 + datetime.timedelta(days=delta)
    return d2.strftime(DATE_FORMAT)


def weekday(day):
    d1 = datetime.datetime.strptime(day, DATE_FORMAT)
    # monday => 1, tuesday => 2,  and so on
    return d1.weekday() + 1


def weekday_str(day):
    return WEEKDAY_DICT.get(weekday(day), weekday(day))


def day_range(day, interval):
    if interval < 0:
        day = add_day(day, interval + 1)
        interval = -interval
    return [add_day(day, i) for i in range(interval)]
