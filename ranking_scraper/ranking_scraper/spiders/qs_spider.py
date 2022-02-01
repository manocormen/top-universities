import scrapy


class QsSpiderSpider(scrapy.Spider):
    name = 'qs_spider'
    allowed_domains = ['topuniversities.com']
    start_urls = ['https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3516175.txt?1643723564?v=1643729848861']

    def parse(self, response):
        data = response.json()  # Convert json to dict
        ranking_data = data["data"]

        for university in ranking_data:
            yield university