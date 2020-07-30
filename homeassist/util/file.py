#!/usr/bin/env python
# encoding: utf-8
# Created by Keeson <coolkeeson@Hotmail.com> at 2019-05-22    
"""
   Desc:
"""
import csv
import os



def iterate_csv(path):
    with open(path) as f:
        is_header = True
        for line in f:
            if is_header:
                is_header = False
                continue
            yield line.strip().split(',')


def list_csv(dir_path):
    file_list = []
    for path in os.listdir(dir_path):
        path = os.path.join(dir_path, path)
        if path.endswith(".csv"):
            file_list.append(path)
    return file_list


def list_file(dir_path):
    file_list = []
    for path in os.listdir(dir_path):
        path = os.path.join(dir_path, path)
        file_list.append(path)
    return file_list


def read_single_csv_in_dir(dir_path):
    f = list_csv(dir_path)[0]
    return csv.DictReader(open(f, "r"))


def list_sol(dir_path):
    file_list = []
    for path in os.listdir(dir_path):
        path = os.path.join(dir_path, path)
        if path.endswith(".sol"):
            file_list.append(path)
    return file_list
