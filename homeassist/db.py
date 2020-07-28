# -*- coding: utf-8 -*-
# @file  : db.py
# @author: xiaoyang.wang
# @date  : 2020/7/11
import threading
import click
from sqlalchemy import create_engine
from flask.cli import with_appcontext
from homeassist.models import *

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
                                        # detect_types=pymysql.cursors.DictCursor,
                                        # cursorclass=pymysql.cursors.DictCursor
        )

    return THREAD_LOCAL.db

def close_mysql_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    global THREAD_LOCAL
    if "db" not in THREAD_LOCAL.__dict__:
        return
    if THREAD_LOCAL.db:
        THREAD_LOCAL.db.close()
        THREAD_LOCAL.db = None

def init_db():
    db = get_mysql_db()
    Base.metadata.create_all(db)

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing indicator and create new tables."""
    init_db()
    click.echo("Initialized the database.")

def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_mysql_db)
    app.cli.add_command(init_db_command)


def row2dict(r):
    return {k: r[k] for k in r.keys()}

def serialize_row(res):
    if isinstance(res, list):
        return [row2dict(e) for e in res]
    else:
        return row2dict(res)