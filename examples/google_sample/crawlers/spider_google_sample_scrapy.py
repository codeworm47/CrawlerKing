from scrapy import Selector
from crawl_tools.crawler_scrapy.spider_base import ScrapySpiderBase
from examples.google_sample.data.repository_file import GoogleSampleRepository
from examples.google_sample.data.entity_google_sample import GoogleSampleEntity
from data.repository_base import RepositoryBase
from typing import List
import datetime

"""
It's just an example
"""


class GoogleSampleSpider(ScrapySpiderBase):

    def get_urls(self):
        return ['https://www.google.com/search?q=hello+world']

    def save(self, body: Selector, item_url: str):
        for item in self.__get_all_a_tags(body):
            link_address = item.__getattribute__('href')
            link_title = item.xpath('string(.)').extract()
            entity = GoogleSampleEntity(self.session_id, datetime.datetime.today(),
                                        item_url, link_address, link_title)
            for repository in self.get_data_repositories():
                repository.save(entity)

    def get_default_bulk_size(self) -> int:
        return 1

    def should_crawl_item(self, item_url) -> bool:
        # Since it's a hypothetical situation
        return True

    def get_data_repositories(self) -> List[RepositoryBase]:
        return [GoogleSampleRepository()]

    @staticmethod
    def __get_all_a_tags(body: Selector):
        return body.css('a')
