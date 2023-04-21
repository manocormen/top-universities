import scrapy

from scraper.settings import qs_urls


class QsSpider(scrapy.Spider):
    name = "qs"
    allowed_domains = ["www.topuniversities.com"]
    start_urls = [qs_urls["cs"][2023]]

    def parse(self, response):
        ranking = response.json()["score_nodes"]
        for uni in ranking:
            yield {
                "name": uni["title"],
                "rank": int(uni["rank"]),
            }
