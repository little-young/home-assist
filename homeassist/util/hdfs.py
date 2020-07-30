# -*- coding: utf-8 -*-
"""
Created on Mon Mar 04 14:13:43 2019

@author: yafeng.xu
"""
import os
import time

from hdfs import InsecureClient

from chandler.util.log import *

NAME_NODE_URLS = ["http://binamenode01.luckycoffee.com:50070",
                  "http://binamenode02.luckycoffee.com:50070"]

HDFS_CLIENT = InsecureClient(";".join(NAME_NODE_URLS), user='hadoop')


def exists(hdfs_path):
    return bool(HDFS_CLIENT.status(hdfs_path, strict=False))


def download_data(hdfs_path, local_path, block=True, n_threads=10):
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    is_dir = True
    if "." in hdfs_path.split("/")[-1]:
        is_dir = False

    while block:
        if not HDFS_CLIENT.status(hdfs_path + '/_SUCCESS', strict=False) and is_dir:
            time.sleep(300)
        elif not HDFS_CLIENT.status(hdfs_path, strict=False):
            time.sleep(300)
        else:
            break

    HDFS_CLIENT.download(hdfs_path, local_path, overwrite=True, n_threads=n_threads)
    info("downloaded from hdfs \n from %s\n to %s", hdfs_path, local_path)


def upload_data(hdfs_path, local_path, n_threads=10):
    """
    if self.client.status(hdfs_path,strict=False):
        self.client.delete(hdfs_path)
    """
    HDFS_CLIENT.upload(hdfs_path, local_path, n_threads=n_threads, overwrite=True)
    info("uploaded to hdfs \n from %s\n to %s", local_path, hdfs_path)
