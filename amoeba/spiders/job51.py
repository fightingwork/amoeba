# -*- coding: utf-8 -*-
import scrapy

from amoeba.items import Job51PositionItem

class Job51Spider(scrapy.Spider):

	# 启动爬虫时需要的参数
    name = 'job51'

    # 爬取域范围
    allowed_domains = ['51job.com']

    # 爬虫第一个url地址
    start_urls = ['http://search.51job.com/list/030200,000000,0000,32,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=/']

    def parse(self, response):

    	node_list = response.xpath("//div[@class='dw_table']//div[@class='el']")

    	# 用来存储所有的item字段
    	#items = []

    	for node in node_list:
    		print(node)
    		# 每个for创建一个item ,用来存储信息
    		item = 	Job51PositionItem()
    		# .extract()  讲xpath对象转换位 Unicode字符串
    		item['positionName'] = node.xpath("./p/span/a/text()").extract()[0].strip().encoding("utf-8")
    		item['comName'] = node.xpath("./span[@class='t2']/a/text()").extract()[0].encoding("utf-8")
    		item['workAddress'] = node.xpath("./span[@class='t3']/text()").extract()[0].encoding("utf-8")
    		item['emolument'] = node.xpath("./span[@class='t4']/text()").extract()[0].encoding("utf-8")
    		item['publishdate'] = node.xpath("./span[@class='t5']/text()").extract()[0].encoding("utf-8")

    		yield item
    		#items.append(item)
    	#return items

