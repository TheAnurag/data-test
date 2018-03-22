# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from  scrapy.exporters import JsonItemExporter
import time
import boto3


AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_BUCKET_NAME = 'aj-data-test'
JSON_FILE_NAME = 'test-data.json'

class CleansingPipeline(object):

    def process_item(self, item, spider):
    	item['price_currency']= item['price'][:1]
    	item['price']= (float)(item['price'][1:])
    	item['review_summary']['count']= (int)(item['review_summary']['count'].split(' ')[0])
    	return item


class JsonExportPipeline(object):

    def __init__(self):
    	self.file = open(JSON_FILE_NAME, 'wb')
    	self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)

    def open_spider(self, spider):
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class S3Pipeline(object):

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        pass

    def close_spider(self, spider): 
        s3 = boto3.client('s3', 
            aws_access_key_id='AKIAJCXTW37QIFRHKRPA',
            aws_secret_access_key='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')
        s3.upload_file(JSON_FILE_NAME, AWS_BUCKET_NAME, JSON_FILE_NAME)
	

class PrintPipeline(object):
	def process_item(self, item, spider):
		print(item)
		return item

