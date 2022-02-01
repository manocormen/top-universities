import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class TheRankingScraperItem(scrapy.Item):
    name = scrapy.Field()
    rank = scrapy.Field()


class QsRankingScraperItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags, lambda s: s.strip()), output_processor=TakeFirst())
    rank = scrapy.Field()