FROM continuumio/miniconda3
RUN conda install scrapy
RUN conda install boto3
WORKDIR /app
ADD . /app
CMD scrapy runspider scraptest/spiders/test_spider.py 

