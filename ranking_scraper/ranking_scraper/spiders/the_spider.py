import scrapy


class TheSpiderSpider(scrapy.Spider):
    name = 'the_spider'
    allowed_domains = ['timeshighereducation.com']
    start_urls = ['https://www.timeshighereducation.com/sites/default/files/the_data_rankings/computer_science_rankings_2022_0__059c3663af4eb54c21c21270fa703f58.json']

    def parse(self, response):
        print(response.body)
        pass
