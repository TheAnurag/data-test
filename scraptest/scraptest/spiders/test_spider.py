import scrapy
from scraptest.items import *
from urllib.parse import urljoin


class TestSpider(scrapy.Spider):
    name = "test_spider"
    allowed_domains = ['webscraper.io']
    start_urls = ['http://webscraper.io/test-sites/e-commerce/allinone']
    categories = list()

    CAT_SELECTOR = '.category-link'
    SUBCAT_SELECTOR = '.subcategory-link'
    PRODUCT_SELECTOR = '.title'

    def parse(self, response):
    	for selector in response.css(self.CAT_SELECTOR) :
    		name =  selector.xpath('text()').extract_first().strip()
    		url = selector.xpath('@href').extract_first().strip()
    		url = response.urljoin(url)
    		
    		request = scrapy.Request(url, callback=self.parse_subcat)
    		request.meta['category'] = name
    		
    		yield request

    	
    def parse_subcat(self, response) :
    	for selector in response.css(self.SUBCAT_SELECTOR) :
    		name =  selector.xpath('text()').extract_first().strip()
    		url = selector.xpath('@href').extract_first().strip()
    		url = response.urljoin(url)
    		
    		request = scrapy.Request(url, callback=self.parse_list)
    		request.meta['category'] = response.meta['category']
    		request.meta['sub-category'] = name
    		
    		yield request


    def parse_list(self, response) :
    	for selector in response.css(self.PRODUCT_SELECTOR) :
    		name =  selector.xpath('@title').extract_first().strip()
    		url = selector.xpath('@href').extract_first().strip()
    		url = response.urljoin(url)
    		    		
    		request = scrapy.Request(url, callback=self.parse_product)
    		request.meta['name'] = name
    		request.meta['category'] = response.meta['category']
    		request.meta['sub-category'] = response.meta['sub-category']

    		yield request

    def parse_product(self, response) :
	    item = Product()
	    item['name'] = response.meta['name']
	    item['category'] = response.meta['category']
	    item['sub_category'] = response.meta['sub-category']
	    item['url'] = response.url
	    item['price'] = response.css('.price').xpath('text()').extract_first().strip() #[1:]
	    item['description'] = response.css('.description').xpath('text()').extract_first().strip()
	    review_summary = {}
	    review_summary['count'] = response.css('.ratings').xpath('./p/text()').extract_first().strip()
	    review_summary['average_rating'] = len(response.css('.glyphicon-star'))
	    item['review_summary'] = review_summary
	    return item


