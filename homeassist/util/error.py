# -*- coding: utf-8 -*-
# @file  : error
# @author: xiaoyang.wang
# @date  : 2020/7/11


class Error(BaseException):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg