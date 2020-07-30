# encoding: utf-8
from time import time
from homeassist.util.error import Error

CACHE_MEM_DICT = {}
CACHE_TIME_DICT = {}


def check_db(db):
    if db not in CACHE_MEM_DICT:
        CACHE_MEM_DICT[db] = {}
        CACHE_TIME_DICT[db] = {}


def delete(key, db=0):
    """删除键为key的条目"""
    check_db(db)
    if key in CACHE_MEM_DICT[db]:
        del CACHE_MEM_DICT[db][key]
        del CACHE_TIME_DICT[db][key]
    return True


def get(key, db=0):
    check_db(db)
    """获取键key对应的值"""
    if key in CACHE_MEM_DICT[db]:
        if CACHE_TIME_DICT[db][key] == -1 or CACHE_TIME_DICT[db][key] > time():
            return CACHE_MEM_DICT[db][key]
        else:
            delete(key, db)
            return None
    else:
        return None


def set(key, data, expire=-1, db=0):
    """
    :param key:
    :param data:
    :param expire: 时间位expire 单位秒'''
    :param db:
    :return:
    """
    check_db(db)
    CACHE_MEM_DICT[db][key] = data
    if expire == -1:
        CACHE_TIME_DICT[db][key] = -1
    else:
        CACHE_TIME_DICT[db][key] = time() + expire
    return True

def update_expire_time(key, expire=-1, db=0):
    check_db(db)
    if not CACHE_MEM_DICT[db].get(key):
        raise Error(f"not {key} in {db}")
    if expire == -1:
        CACHE_TIME_DICT[db][key] = -1
    else:
        CACHE_TIME_DICT[db][key] = time() + expire
    return True
