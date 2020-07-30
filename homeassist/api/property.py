# -*- coding: utf-8 -*-
# @file  : property.py
# @author: xiaoyang.wang
# @date  : 2020/7/25


from homeassist.db import get_mysql_db, serialize_row

def add_property(**kwargs):
    return