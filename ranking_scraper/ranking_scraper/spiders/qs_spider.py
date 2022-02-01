import scrapy


class QsSpiderSpider(scrapy.Spider):
    name = 'qs_spider'
    allowed_domains = ['topuniversities.com']
    start_urls = ['http://topuniversities.com/']

    def parse(self, response):
        pass
