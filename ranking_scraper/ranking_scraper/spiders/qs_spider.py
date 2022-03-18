import scrapy

from ranking_scraper.items import QsRankingScraperItem
from ranking_scraper.settings import ranking
from scrapy.loader import ItemLoader


class QsSpiderSpider(scrapy.Spider):
    name = 'qs_spider'
    allowed_domains = ['topuniversities.com']
    start_urls = [ranking["urls"][1]]

    def parse(self, response):
        data = response.json()  # Convert json to dict
        ranking_data = data["data"]

        for university in ranking_data:
            l = ItemLoader(item = QsRankingScraperItem(), selector=university)
            l.add_value("name", university["title"])
            l.add_value("rank", university["rank_display"])
            yield l.load_item()