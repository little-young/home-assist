# -*- encoding: utf-8 -*-
"""
@File    : example.py
@Time    : 2020/7/28 0028 01:18
@Author  : delphi.young
@Email   : -
@Software: PyCharm Community Edition
"""


import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import relationship

# Base = declarative_base()
#
# class Users(Base):
#     __tablename__ = 'users'                #表名称
#     id = Column(Integer, primary_key=True) # primary_key=True设置主键
#     name = Column(String(32), index=True, nullable=False) #index=True创建索引， nullable=False不为空。
#     age = Column(Integer, default=18)        #数字字段
#     email = Column(String(32), unique=True)  #设置唯一索引
#     ctime = Column(DateTime, default=datetime.datetime.now) #设置默认值为当前时间（注意千万不要datetime.datetime.now（））
#     extra = Column(Text, nullable=True)         #文本内容字段
#     __table_args__ = (
#         # UniqueConstraint('id', 'name', name='uix_id_name'), #设置联合唯一索引
#         # Index('ix_id_name', 'name', 'extra'),                #设置联合索引
#     )
#
#
#
#
# class Hosts(Base):
#     __tablename__ = 'hosts'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(32), index=True)
#     ctime = Column(DateTime, default=datetime.datetime.now)
#
#
# # ##################### 一对多示例 #########################
# class Hobby(Base):
#     __tablename__ = 'hobby'
#     id = Column(Integer, primary_key=True)
#     caption = Column(String(50), default='篮球')
#
#
# class Person(Base):
#     __tablename__ = 'person'
#     nid = Column(Integer, primary_key=True)
#     name = Column(String(32), index=True, nullable=True)
#     hobby_id = Column(Integer, ForeignKey("hobby.id"))
#
#     # 与生成表结构无关，仅用于查询方便
#     hobby = relationship("Hobby", backref='pers')
#
#
# # ##################### 多对多示例 #########################
#
# class Server2Group(Base):
#     __tablename__ = 'server2group'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     server_id = Column(Integer, ForeignKey('server.id'))
#     group_id = Column(Integer, ForeignKey('group.id'))
#
#
# class Group(Base):
#     __tablename__ = 'group'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64), unique=True, nullable=False)
#
#     # 与生成表结构无关，仅用于查询方便
#     servers = relationship('Server', secondary='server2group', backref='groups')
#
#
# class Server(Base):
#     __tablename__ = 'server'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     hostname = Column(String(64), unique=True, nullable=False)
#
#
# def init_db():
#     """
#     根据类创建数据库表
#     :return:
#     """
#     engine = create_engine(
#         "mysql+pymysql://webproject:web@192.168.1.18:3306/web?charset=utf8",
#         max_overflow=0,  # 超过连接池大小外最多创建的连接
#         pool_size=5,  # 连接池大小
#         pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
#         pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
#     )
#
#     Base.metadata.create_all(engine)
#
# if __name__ == '__main__':
#     init_db()