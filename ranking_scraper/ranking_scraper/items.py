import scrapy


class TheRankingScraperItem(scrapy.Item):
    name = scrapy.Field()
    rank = scrapy.Field()