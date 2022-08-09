from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def start_crawler():

    process = CrawlerProcess(get_project_settings())

    process.crawl('printables')
    process.start()

if __name__==("__main__"):
    start_crawler()
