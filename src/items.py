'''
Created on Aug 25, 2015

@author: v-shayi
'''
import scrapy

class indexItem(scrapy.Item):
    data = scrapy.Field()
    year = scrapy.Field()
    value = scrapy.Field()
    unit = scrapy.Field()