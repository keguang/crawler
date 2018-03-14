# -*- coding: utf-8 -*-
from sqlalchemy import Column,String,Integer,DateTime

from . import Base
import datetime
class YingYongBao(Base):
    __tablename__ = 'yingyongbao'

    name=Column(String(30),primary_key=True,nullable=False)

    # def __init__(self,ip_port,source,type=None,level=None,location=None,speed=None):
    #     self.ip_port=ip_port
    #     self.type=type
    #     self.level=level
    #     self.location=location
    #     self.speed=speed
    #     self.source=source
    #     self.indate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")