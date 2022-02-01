import scrapy


class TheSpiderSpider(scrapy.Spider):
    name = 'the_spider'
    allowed_domains = ['timeshighereducation.com']
    start_urls = ['http://timeshighereducation.com/']

    def parse(self, response):
        pass
