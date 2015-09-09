#coding:utf-8
'''
Created on Aug 25, 2015

@author: v-shayi
'''
from scrapy.spiders import Spider
from scrapy.selector import Selector
from src.items import indexItem
from scrapy.http.request import Request

str1 = u'养殖'
str2 = u'猪'
str3 = u'畜'
domainURL = "http://www.bjny.gov.cn"

class indexSpider(Spider):
    name = "indexSpider"
    allowed_domains = ["bjny.gov.cn"]
    start_urls = ["http://www.bjny.gov.cn/nyj/232120/327371/Index.html"]
    
    def parse(self, response):
        sel = Selector(response)
        link = '//li/a[contains(text(), "%s")]' % str1
        sites = sel.xpath(link)
        
        for site in sites:
            siteURL = site.xpath('@href').extract()
            year = site.xpath('text()').re(r'\d{4}')
            yield Request(url= domainURL + siteURL[0], callback=self.parse_page2, meta={'year': year})
        
    def parse_page2(self, response):
        year = response.meta['year']
        responseUrl = response.url
        sel = Selector(response)
        rows = sel.xpath('//div[contains(@id, "oom")]/table/tbody/tr')
        items = []
        
        if len(rows) > 0:
            for row in rows:
                cols = row.xpath('td')
                if len(cols) > 3:
                    link = './/*[contains(text(), "%s")]/text()' % str2
                    dataContent = cols[0].xpath(link).extract()
                    if len(dataContent) > 0:
                        item = indexItem()
                        item['data'] = dataContent
                        item['year'] = year
                        item['unit'] = cols[1].xpath('.//*/text()').extract()
                        item['value'] = cols[2].xpath('.//*/text()').extract()
                        items.append(item)
                        yield item
                    