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
    if len(rank) == 7:  # E.g. 201-300 --> 201
        rank = rank[:3]
    return int(rank)


class TheItem(scrapy.Item):
    name = scrapy.Field()
    rank = scrapy.Field()


class TheItemLoader(ItemLoader):
    default_item_class = TheItem  # Special var to tie Item and ItemLoader
    default_output_processor = TakeFirst()  # Since usual default is Identity()
    rank_in = MapCompose(format_)
