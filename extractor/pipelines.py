# -*- coding: utf-8 -*-

import json

class JsonPipeline(object):

    my_items = []

    def close_spider(self, spider):
        with open('items.json', 'wb') as f:
            f.write(json.dumps(self.my_items))
            f.write("\n")

    def process_item(self, item, spider):
        self.my_items.append(dict(item))
        return item
