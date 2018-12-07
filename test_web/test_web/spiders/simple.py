# -*- coding: utf-8 -*-
import scrapy

l = [None, None]

class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = ['18.18.186.19:7000']
    start_urls = ['http://18.18.186.19:7000/']

    def parse(self, response):
        # 2的n次方
        for i in l:
            yield scrapy.Request(url='http://18.18.186.19:7000/', callback=self.parse, dont_filter=True)

