# -*- coding: utf-8 -*-
# @file  : db.py
# @author: xiaoyang.wang
# @date  : 2020/7/11
import pymysql
import threading
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from homeassist import config

THREAD_LOCAL = threading.local()


def get_mysql_db():
    global THREAD_LOCAL
    if "db" not in THREAD_LOCAL.__dict__:
        THREAD_LOCAL.db = None
    if not THREAD_LOCAL.db:
        THREAD_LOCAL.db = create_engine(config.DB_ENGINE_URL,
                                        max_overflow=2, #超过连接池大小之后，允许最大扩展连接数；
                                        pool_size=5,   #连接池大小
                                        pool_timeout=30,#连接池如果没有连接了，最长等待时间
                                        pool_recycle=-1,#多久之后对连接池中连接进行一次回收
        )
        # THREAD_LOCAL.db.

    return THREAD_LOCAL.db


def row2dict(r):
    return {k: r[k] for k in r.keys()}

def serialize_row(res):
    if isinstance(res, list):
        return [row2dict(e) for e in res]
    else:
        return row2dict(res)