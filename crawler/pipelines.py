# -*- coding: utf-8 -*-

# Define your item pipelines here
import os

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline

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



class FilesPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        """
        重命名模块
        """
        path = os.path.join('tmp', ''.join([str(int(time.time()*1000)),'.apk']))
        return path

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item