# -*- coding: utf-8 -*-
import scrapy


class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = ['18.18.186.19:7000']
    start_urls = ['http://18.18.186.19:7000/']

    def parse(self, response):
        yield scrapy.Request(url='http://18.18.186.19:7000/', callback=self.parse, dont_filter=True)

