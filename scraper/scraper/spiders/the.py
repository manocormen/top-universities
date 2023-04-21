import scrapy

from scraper.items import UniItemLoader
from scraper.settings import the_urls


class TheSpider(scrapy.Spider):
    name = "the"

    def start_requests(self):
        yield scrapy.Request(url=the_urls[self.subject][int(self.year)])

    def parse(self, response):
        ranking = response.json()["data"]
        for uni in ranking:
            loader = UniItemLoader()
            loader.add_value("name", uni["name"])
            loader.add_value("rank", uni["rank"])
            yield loader.load_item()
