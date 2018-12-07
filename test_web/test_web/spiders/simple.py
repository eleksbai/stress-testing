# -*- coding: utf-8 -*-
import scrapy

base = '18.18.248.111:5000'
url_domain = base
url = 'http://{}/'.format(base)

c = 0
class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = [url_domain]
    start_urls = [url]

    def parse(self, response):
        # 2的n次方 ,到达1000限制扩散
        global c
        c += 1
        if c < 1000:
            for i in [None, None]:
                yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
        else:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

