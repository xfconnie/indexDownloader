#coding:utf-8
'''
Created on Aug 24, 2015

@author: v-shayi
'''
import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', '-o', 'output.xml', '-t', 'xml', 'indexSpider'])

if __name__ == '__main__':
    main()