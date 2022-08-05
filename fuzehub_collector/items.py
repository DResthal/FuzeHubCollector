# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class ModelItem(scrapy.Item):
    
    id = scrapy.Field()
    name = scrapy.Field()
    likes = scrapy.Field()
    url = scrapy.Field()
    downloads = scrapy.Field()
    last_update = scrapy.Field()
    images = scrapy.Field()

