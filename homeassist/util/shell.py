#!/usr/bin/env python
# encoding: utf-8
# Created by Keeson <coolkeeson@Hotmail.com> at 2019-05-22    
"""
   Desc:
"""
import os

def mkdir(path):
    os.makedirs(path, exist_ok=True)
    return path


def exists(path):
    return os.path.exists(path)


def touch(path):
    open(path, 'a').close()
