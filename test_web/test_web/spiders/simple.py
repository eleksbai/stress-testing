# -*- coding: utf-8 -*-
import scrapy


c = 0
class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = ['18.18.186.19:7000']
    start_urls = ['http://18.18.186.19:7000/']

    def parse(self, response):
        # 2的n次方 ,到达1000限制扩散
        global c
        c += 1
        if c < 1000:
            for i in [None, None]:
                yield scrapy.Request(url='http://18.18.186.19:7000/', callback=self.parse, dont_filter=True)
        else:
            yield scrapy.Request(url='http://18.18.186.19:7000/', callback=self.parse, dont_filter=True)

