import scrapy

from ranking_scraper.items import TheRankingScraperItem


class TheSpiderSpider(scrapy.Spider):
    name = 'the_spider'
    allowed_domains = ['timeshighereducation.com']
    start_urls = ['https://www.timeshighereducation.com/sites/default/files/the_data_rankings/computer_science_rankings_2022_0__059c3663af4eb54c21c21270fa703f58.json']

    def parse(self, response):
        data = response.json()  # Convert json to dict
        ranking_data = data["data"]
        
        item = TheRankingScraperItem()
        for university in ranking_data:
            item["name"] = university["name"]
            item["rank"] = university["rank"]
            yield item