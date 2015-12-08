# -*- coding: utf-8 -*-

import json

class JsonPipeline(object):

    def __init__(self):
        self.file = open('items.json', 'wb')

    def process_item(self, item, spider):
        line = "{}\n".format(json.dumps(dict(item)))
        self.file.write(line)
        return item

