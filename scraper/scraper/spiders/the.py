import scrapy

from scraper.items import UniItemLoader
from scraper.settings import the_urls


class TheSpider(scrapy.Spider):
    name = "the"
    allowed_domains = ["www.timeshighereducation.com"]
    start_urls = [the_urls["cs"][2023]]

    def parse(self, response):
        ranking = response.json()["data"]
        for uni in ranking:
            loader = UniItemLoader()
            loader.add_value("name", uni["name"])
            loader.add_value("rank", uni["rank"])
            yield loader.load_item()
