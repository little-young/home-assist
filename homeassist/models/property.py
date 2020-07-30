# -*- coding: utf-8 -*-
# @file  : property
# @author: xiaoyang.wang
# @date  : 2020/7/25
import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index, BIGINT
from . import Base

'''
CREATE TABLE IF NOT EXISTS mvp.t_property
(
    id  BIGINT PRIMARY KEY AUTOINCREMENT,
    property_name  TEXT UNIQUE NOT NULL,
    legal_person  TEXT NOT NULL,
    license_no    TEXT NOT NULL,
    level        INTEGER NOT NULL DEFAULT 0,-- 物业等级
    contact_name TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT,
    address TEXT,
    create_time  DATETIME,
    update_time  DATETIME,
    is_delete  TINYINT,
    EXTEND_JSON TEST
);
'''

class Property(Base):
    __tablename__ = 't_property'                #表名称
    id = Column(Integer, index=True, primary_key=True) # primary_key=True设置主键
    property_name = Column(String(128), nullable=False)
    legal_person = Column(String(32), nullable=False)
    license_no = Column(Text, nullable=False)
    level = Column(Integer)
    contact_name = Column(String(32), nullable=False)
    contact_number = Column(String(32), nullable=False)
    email= Column(String(32), nullable=False)
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime)
    extend_json = Column(Text)
    is_delete = Column(Integer, default=0)

    __table_args__ = (
        {"useexisting": True}
    )

    def __repr__(self):
        return '[member {},{}]'.format(self.id, self.property_name)
