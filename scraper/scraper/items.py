# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


def format_(rank):
    rank = rank.removeprefix("=")
    rank = rank.removesuffix("+")
    if "-" in rank or "–" in rank:
        # E.g. 100-200 -> 100, 75-100 -> 75, 50-75 -> 50
        rank = rank[:3] if len(rank) == 7 else rank[:2]
    return int(rank)


class UniItem(scrapy.Item):
    name = scrapy.Field()
    rank = scrapy.Field()


class UniItemLoader(ItemLoader):
    default_item_class = UniItem  # Special var to tie Item and ItemLoader
    default_output_processor = TakeFirst()  # Since usual default is Identity()
    rank_in = MapCompose(format_)
