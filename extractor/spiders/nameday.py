# -*- coding: utf-8 -*-
#
# Scrapy spider which extracts names for today from http://www.nimipaivat.fi.
#
# Author: Jarno Tuovinen
#
# License: MIT
#

import re
import datetime
import scrapy
from extractor.items import NamedayItem

date_pattern = re.compile('\d+')

nameday_url = "http://www.nimipaivat.fi/"
# Create URLs for each day
urls = []
mlen = (31,28,31,30,31,30,31,31,30,31,30,31)
for currentmonth in range (len(mlen)):
    for day in range (mlen[currentmonth]):
        url = "{}{}.{}.".format(nameday_url, day+1, currentmonth+1)
        urls.append(url)

class NamedaySpider(scrapy.Spider):
    name = "nameday"
    allowed_domains = ["nimipaivat.fi"]
    start_urls = urls

    def parse(self, response):
        # Extract
        date = response.xpath("/html/body/div[@class='kontaineri']/div[@class='eka']/h1/text()").extract_first()
        official_names = response.xpath("/html/body/div[@class='kontaineri']/div[@class='eka']/p[1]/strong/a/text()").extract()
        swedish_names = response.xpath("/html/body/div[@class='kontaineri']/div[@class='eka']/p[2]/strong/a/text()").extract()
        sami_names = response.xpath("/html/body/div[@class='kontaineri']/div[@class='eka']/p[3]/strong/a/text()").extract()
        orthodox_names = response.xpath("/html/body/div[@class='kontaineri']/div[@class='eka']/p[4]/strong/a/text()").extract()
        unofficial_names = response.xpath("/html/body/div[@class='kontaineri']/div[@class='eka']/p[5]/strong/a/text()").extract()

        # Extract day and month from date string
        extracted_date = date_pattern.findall(date)

        # Populate the item
        item = NamedayItem()
        item['day'] = extracted_date[0]
        item['month'] = extracted_date[1]
        item['official_names'] = official_names
        item['swedish_names'] = swedish_names
        item['sami_names'] = sami_names
        item['orthodox_names'] = orthodox_names
        item['unofficial_names'] = unofficial_names

        # Return item to pipeline
        return item

