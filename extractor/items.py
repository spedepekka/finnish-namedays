# -*- coding: utf-8 -*-

import scrapy

class NamedayItem(scrapy.Item):
    day = scrapy.Field()
    month = scrapy.Field()
    orthodox_names = scrapy.Field()
    unofficial_names = scrapy.Field()

