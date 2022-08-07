# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from fuzehub_collector.db import Connection


class FuzehubCollectorPipeline:
    def __init__(self):
        self.conn = Connection("printables")

    def process_item(self, item, spider):

        item['url'] = f"https://www.printables.com/model/{item['url']}"

        self.conn.save_item(item)

        return item
