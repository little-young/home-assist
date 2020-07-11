#!/usr/bin/env python
# encoding: utf-8
# Created by Keeson <coolkeeson@Hotmail.com> at 2019-04-16    
"""
   Desc:
"""

import logging

LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'

LOGGER = None


def _get_logger():
    global LOGGER
    if LOGGER:
        return LOGGER

    LOGGER = logging.getLogger("user-reach-algorithm")
    fmt = logging.Formatter(LOG_FORMAT)
    handler = logging.StreamHandler()
    handler.setFormatter(fmt)
    LOGGER.addHandler(handler)
    LOGGER.setLevel(logging.INFO)
    return LOGGER


def error(msg, *args, **kwargs):
    _get_logger().error(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    _get_logger().warning(msg, *args, **kwargs)


def warn(msg, *args, **kwargs):
    warning(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    _get_logger().info(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    _get_logger().debug(msg, *args, **kwargs)
