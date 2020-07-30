#!/usr/bin/env python
# encoding: utf-8
# Created by Keeson <coolkeeson@Hotmail.com> at 2019/11/21    
"""
   Desc:
"""

# encoding=utf-8
# Generated by cpy
# 2016-04-11 20:40:38.174634
from pyssdb import Client

from homeassist.util.log import warn

try:
    SSDB_CLIENT = Client(host='127.0.0.1', port=8888)
except:
    SSDB_CLIENT = None
    warn("init ssdb fail")


def get(key):
    res = SSDB_CLIENT.get(key)
    if res:
        return res.decode()
    return None


def delete(key):
    SSDB_CLIENT.delete(key)


def set(key, value):
    SSDB_CLIENT.set(key, value)


def setx(key, value, seconds):
    SSDB_CLIENT.setx(key, value, int(seconds))


def expire(key, seconds):
    SSDB_CLIENT.expire(key, int(seconds))
