# -*- coding: utf-8 -*-

import scrapy

class NamedayItem(scrapy.Item):
    official_names = scrapy.Field()
    swedish_names = scrapy.Field()
    sami_names = scrapy.Field()
    orthodox_names = scrapy.Field()
    unofficial_names = scrapy.Field()

