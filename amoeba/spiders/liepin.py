# -*- coding: utf-8 -*-
import scrapy


class LiepinSpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['www.liepin.com']
    base_url = ['https://passport.liepin.com/e/account#sfrom=click-pc_homepage-front_navigation-ecomphr_new']

    def parse(self, response):
    	pass
