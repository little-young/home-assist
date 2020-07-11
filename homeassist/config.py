# -*- coding: utf-8 -*-
# @file  : config.py
# @author: xiaoyang.wang
# @date  : 2020/7/11

from enum import Enum

class ReturnCode(Enum):
    SUCCESS = 10000
    FAIL = 61001
    NOT_SUPPORT_MSG = "Not Support"


class CacheDataBase(Enum):
    MEM_DB = 1
    MEM_DB_EXP_SECS = 3600