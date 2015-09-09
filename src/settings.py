'''
Created on Aug 25, 2015

@author: v-shayi
'''
BOT_NAME = 'src'
SPIDER_MODULES = ['src.spiders']
NEWSPIDER_MODULE = 'src.spiders'
DEFAULT_ITEM_CLASS = 'src.items.indexItem'

ITEM_PIPELINES = {'src.pipelines.MyPipeline'}