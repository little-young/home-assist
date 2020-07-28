# -*- coding: utf-8 -*-
# @file  : member.py
# @author: xiaoyang.wang
# @date  : 2020/7/22

import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index, BIGINT
from . import Base

# CREATE TABLE IF NOT EXISTS mvp.t_member
# (
#     id  BIGINT PRIMARY KEY AUTOINCREMENT,
#     name  TEXT UNIQUE NOT NULL,
#     nick_name  TEXT  DEFAULT '用户',
#     password  TEXT  NOT NULL,
#     role  INT  NOT NULL DEFAULT 99,
#     property_id  INT  NOT NULL,
#     create_time  DATETIME,
#     update_time  DATETIME,
#     is_delete  TINYINT DEFAULT 0,
#     EXTEND_JSON TEST
# );

class Member(Base):
    __tablename__ = 't_member'                #表名称
    id = Column(Integer, index=True, primary_key=True) # primary_key=True设置主键
    name = Column(String(32), index=True, nullable=False) #index=True创建索引， nullable=False不为空。
    nick_name = Column(String(32), default='用户')
    password = Column(Text, nullable=False)
    role = Column(Integer, nullable=False, default=99)
    property_id = Column(Integer, index=True, nullable=False)
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime)
    extend_json = Column(Text)
    is_delete = Column(Integer, default=0)

    __table_args__ = (
        {"useexisting": True}
    )

    def __repr__(self):
        return '[member {},{}]'.format(self.id, self.name)