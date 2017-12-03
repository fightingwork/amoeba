# -*- coding: utf-8 -*-
import scrapy

from selenium import webdriver

class LiepinSpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['www.liepin.com']
    base_url = ['https://passport.liepin.com/e/account#sfrom=click-pc_homepage-front_navigation-ecomphr_new']

    def parse(self, response):
    	driver = webdriver.Chrome()
	driver.get(self.base_url)

	#driver.find_element_by_id("kw").click()
	#driver.find_element_by_id("kw").send_keys("123")
	#driver.find_element_by_id("su").click()
	pass
