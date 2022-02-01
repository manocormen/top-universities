import scrapy

from ranking_scraper.items import QsRankingScraperItem
from scrapy.loader import ItemLoader


class QsSpiderSpider(scrapy.Spider):
    name = 'qs_spider'
    allowed_domains = ['topuniversities.com']
    start_urls = ['https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3516175.txt?1643723564?v=1643729848861']

    def parse(self, response):
        data = response.json()  # Convert json to dict
        ranking_data = data["data"]

        for university in ranking_data:
            l = ItemLoader(item = QsRankingScraperItem(), selector=university)
            l.add_value("name", university["title"])
            l.add_value("rank", university["rank_display"])
            yield l.load_item()