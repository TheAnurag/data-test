# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from  scrapy.exporters import JsonItemExporter
import time


class CleansingPipeline(object):

    def process_item(self, item, spider):
    	item['price_currency']= item['price'][:1]
    	item['price']= (float)(item['price'][1:])
    	item['review_summary']['count']= (int)(item['review_summary']['count'].split(' ')[0])
    	return item


class JsonExportPipeline(object):

    def __init__(self):
    	fname = 'test-' + time.strftime('%Y%m%d-%H%M%S') + '.json'
    	self.file = open(fname, 'wb')
    	self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)

    def spider_opened(self, spider):
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
	

class PrintPipeline(object):
	def process_item(self, item, spider):
		print(item)
		return item

