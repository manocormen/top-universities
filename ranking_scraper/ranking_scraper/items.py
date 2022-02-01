import scrapy


class RankingScraperItem(scrapy.Item):
    name = scrapy.Field()
    rank = scrapy.Field()