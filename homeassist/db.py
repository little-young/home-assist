# -*- coding: utf-8 -*-
# @file  : db.py
# @author: xiaoyang.wang
# @date  : 2020/7/11
import threading
import pymysql
from sqlalchemy import create_engine

THREAD_LOCAL = threading.local()


def get_mysql_db():
    global THREAD_LOCAL
    if "db" not in THREAD_LOCAL.__dict__:
        THREAD_LOCAL.db = None
    if not THREAD_LOCAL.db:
        THREAD_LOCAL.db = pymysql.connect(

        )
        # THREAD_LOCAL.db.row_factory = pymysql

    return THREAD_LOCAL.db


def row2dict(r):
    return {k: r[k] for k in r.keys()}

def serialize_row(res):
    if isinstance(res, list):
        return [row2dict(e) for e in res]
    else:
        return row2dict(res)