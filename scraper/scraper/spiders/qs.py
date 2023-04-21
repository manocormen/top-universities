import scrapy

from scraper.settings import qs_urls


class QsSpider(scrapy.Spider):
    name = "qs"

    def start_requests(self):
        yield scrapy.Request(url=qs_urls[self.subject][int(self.year)])

    def parse(self, response):
        ranking = response.json()["score_nodes"]
        for uni in ranking:
            yield {
                "name": uni["title"],
                "rank": int(uni["rank"]),
            }
