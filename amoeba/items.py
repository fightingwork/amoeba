# -*- coding: utf-8 -*-

import scrapy


# 51job职位条目
class Job51PositionItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名
   	positionName=scrapy.Field()
   	comName=scrapy.Field()
   	workAddress=scrapy.Field()
   	emolument=scrapy.Field()
   	publishdate=scrapy.Field()


