# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class FuzehubCollectorPipeline:
    def __init__(self):
        self.con = sqlite3.connect("/var/lib/databases/fuzehubmodels.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS models(
            id REAL PRIMARY KEY,
            name TEXT,
            likes REAL,
            url TEXT,
            downloads REAL,
            last_update TEXT,
            images TEXT)
        """
        )

    def process_item(self, item, spider):
        self.cur.execute(
            """INSERT OR REPLACE INTO models VALUES (?,?,?,?,?,?,?)""",
            (
                item["id"],
                item["name"],
                item["likes"],
                item["downloads"],
                item["url"],
                item["last_update"],
                str(item["images"]),
            )
        )
        self.con.commit()
        return item
