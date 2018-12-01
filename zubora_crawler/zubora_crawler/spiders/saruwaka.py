# -*- coding: utf-8 -*-
import scrapy


class SaruwakaSpider(scrapy.Spider):
    name = 'saruwaka'
    allowed_domains = ['saruwakakun.com/life/recipe']
    start_urls = ['http://saruwakakun.com/life/recipe/']

    def parse(self, response):
        pass
