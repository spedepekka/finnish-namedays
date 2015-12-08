# -*- coding: utf-8 -*-
#
# Scrapy spider which extracts names for today from http://www.nimipaivat.fi.
#
# Author: Jarno Tuovinen
#
# License: MIT
#

import datetime
import scrapy
from extractor.items import NamedayItem

nameday_url = "http://www.nimipaivat.fi/"
# Resolve day and month
now = datetime.datetime.now()
day = now.day
month = now.month
# Create URL for today
today_url = "{}{}.{}.".format(nameday_url, day, month)

class NamedaySpider(scrapy.Spider):
    name = "nameday"
    allowed_domains = ["nimipaivat.fi"]
    start_urls = [today_url]

    def parse(self, response):
        items = []

        # Extract names
        official_names = response.xpath("/html/body/div[@class='kontaineri']/div[@class='eka']/p[1]/strong/a/text()").extract()
        swedish_names = response.xpath("/html/body/div[@class='kontaineri']/div[@class='eka']/p[2]/strong/a/text()").extract()
        sami_names = response.xpath("/html/body/div[@class='kontaineri']/div[@class='eka']/p[3]/strong/a/text()").extract()
        orthodox_names = response.xpath("/html/body/div[@class='kontaineri']/div[@class='eka']/p[4]/strong/a/text()").extract()
        unofficial_names = response.xpath("/html/body/div[@class='kontaineri']/div[@class='eka']/p[5]/strong/a/text()").extract()

        # Create new item
        item = NamedayItem()
        # Populate the item
        item['official_names'] = official_names
        item['swedish_names'] = swedish_names
        item['sami_names'] = sami_names
        item['orthodox_names'] = orthodox_names
        item['unofficial_names'] = unofficial_names
        # Save item
        items.append(item)

        # Return items to pipeline
        return items

