# -*- coding: utf-8 -*-
import scrapy
import json


class YingyongbaoSpider(scrapy.Spider):
    name = 'yingyongbao'
    allowed_domains = ['http://sj.qq.com/myapp/cate/appList.htm']

    def start_requests(self):
        for page in range(0, 1):
            page_offset = page * 20
            start_url = 'http://sj.qq.com/myapp/cate/appList.htm?orgame=1&categoryId=0&pageSize=20&pageContext=' + str(
                page_offset)
            yield scrapy.Request(url=start_url, method="get", callback=self.parse)

    def parse(self, response):
        response = json.loads(response.body)
        app_list = response['obj']
        for app in app_list:
            name = app['appName']
            yield {"name": name}
        pass
