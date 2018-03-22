# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    price_currency = scrapy.Field()
    review_summary = scrapy.Field() #ReviewSummary
    image_url = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()


class ReviewSummary(scrapy.Item):
    count = scrapy.Field()
    average_rating = scrapy.Field()
