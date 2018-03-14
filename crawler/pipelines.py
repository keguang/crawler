# -*- coding: utf-8 -*-

# Define your item pipelines here
from model import Base,engine,loadSession
from model import ttsrc


class YingYongBaoPipeline(object):
    #搜索Base的所有子类，并在数据库中生成表
    Base.metadata.create_all(engine)

    def process_item(self, item, spider):
        if spider.name=='yingyongbao':
            model = ttsrc.YingYongBao(
                name=item['name'],
            )
            session = loadSession()
            session.add(model)
            session.commit()
            return item