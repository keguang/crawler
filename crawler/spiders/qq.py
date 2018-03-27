# -*- coding: utf-8 -*-
import scrapy

# 下载图片实例
class QqSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['qq.com']
    start_urls = ['http://qq.com/']

    def getHeaders(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, sdch, br",
            "accept-language": "zh-CN,zh;q=0.8",
            "cache-control": "max-age=0",
            "upgrade-insecure-requests": "1",
            # "host":"agent.sj.qq.com",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
        }
        return headers

    def start_requests(self):
        url = 'http://sj.qq.com/myapp/'
        for i in range(0,100):
            yield scrapy.Request(url=url, method='get', headers=self.getHeaders(),dont_filter=True, callback=self.parse,
                                 meta={'cookiejar': 1})


    def parse(self, response):
        # base_url='http://timgsa.baidu.com'
        download_href=['http://imtt.dd.qq.com/16891/4ABF38D08DEA2C5538347D08D74DC337.apk?fsname=com.subject.ysh_4.1_20171115.apk&csr=1bbd']
        item=MyItem()
        # item['image_urls']= urlparse.urljoin(base_url, download_href)
        item['image_urls']= download_href
        print(item)
        yield item

