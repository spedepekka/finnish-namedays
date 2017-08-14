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

        official_names = []
        swedish_names = []
        same_names = []
        orthodox_names = []
        unofficial_names = []

        date = response.xpath("/html/body/div/div/div/h1/text()").extract_first()
        ps = response.xpath("/html/body/div[@class='container']/div[@class='row']/div[@class='col-md-6']/p")
        for p in ps:
            if "Nimi" in p.extract():
                official_names = p.xpath("strong/a/text()").extract()
            elif "Ruotsinkieli" in p.extract():
                swedish_names = p.xpath("strong/a/text()").extract()
            elif "Saamenkieli" in p.extract():
                same_names = p.xpath("strong/a/text()").extract()
            elif "Ortodoksista" in p.extract():
                orthodox_names = p.xpath("strong/a/text()").extract()
            elif "virallista" in p.extract():
                unofficial_names = p.xpath("strong/a/text()").extract()

        # Extract day and month from date string
        extracted_date = date_pattern.findall(date)

        # Populate the item
        item = NamedayItem()
        item['day'] = extracted_date[0]
        item['month'] = extracted_date[1]
        # Uncomment these lines to make this crawler crawl forbidden names
        # item['official_names'] = official_names
        # item['swedish_names'] = swedish_names
        # item['same_names'] = same_names
        item['orthodox_names'] = orthodox_names
        item['unofficial_names'] = unofficial_names

        # Return item to pipeline
        return item

