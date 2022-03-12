import scrapy

from ranking_scraper.items import TheRankingScraperItem
from ranking_scraper.settings import ranking_urls


class TheSpiderSpider(scrapy.Spider):
    name = 'the_spider'
    allowed_domains = ['timeshighereducation.com']
    start_urls = [ranking_urls[0]]

    def parse(self, response):
        data = response.json()  # Convert json to dict
        ranking_data = data["data"]
        
        item = TheRankingScraperItem()
        for university in ranking_data:
            item["name"] = university["name"]
            item["rank"] = university["rank"]
            yield item