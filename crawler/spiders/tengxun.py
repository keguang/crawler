# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.http.cookies import CookieJar  # 该模块继承自内置的http.cookiejar,操作类似

# cookie实例
class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['sj.qq.com']
    start_urls = ['http://sj.qq.com/']

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
        for i in range(0,10):
            yield scrapy.Request(url=url, method='get', headers=self.getHeaders(),dont_filter=True, callback=self.parse,
                                 meta={'cookiejar': 1})

    def parse(self, response):
        # 实例化一个cookiejar对象
        cookie_jar = CookieJar()
        file = open('cookie.txt', 'a+')

        cookie_jar.extract_cookies(response, response.request)
        _t = str(int(time.time() * 1000))

        session_id = ''
        for cookie in cookie_jar:
            cookie_str = str(cookie)
            session_id = cookie_str[21:-21]
            file.write(session_id + "\n")


        url = 'http://agent.sj.qq.com/behaviour.do?aid=myappWebBehaviour&post=%09' + session_id + '%09details%09null%09btn_download%09com.subject.ysh%09%E5%8E%9F%E5%A7%8B%E4%BC%9A&t=' + _t
        file.write(url+"\n")
        cookie_jar.clear()
        yield scrapy.Request(url=url, method='get', headers=self.getHeaders())

        pass

