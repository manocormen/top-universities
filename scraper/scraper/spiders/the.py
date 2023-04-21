import scrapy

from scraper.items import UniItemLoader


class TheSpider(scrapy.Spider):
    name = "the"
    allowed_domains = ["www.timeshighereducation.com"]
    start_urls = ["https://www.timeshighereducation.com/sites/default/files/the_data_rankings/computer_science_rankings_2023_0__0f480cc165726b46cd42a2f6fa025532.json"]

    def parse(self, response):
        ranking = response.json()["data"]
        for uni in ranking:
            loader = UniItemLoader()
            loader.add_value("name", uni["name"])
            loader.add_value("rank", uni["rank"])
            yield loader.load_item()
