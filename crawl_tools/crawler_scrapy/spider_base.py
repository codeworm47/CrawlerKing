import scrapy
from abc import abstractmethod
from utils.helpers.http_helper import HttpHelper
from utils.session import Session
from scrapy.selector import Selector
from typing import List
from data.repository_base import RepositoryBase


class ScrapySpiderBase(scrapy.Spider):
    name = None
    sitemap_url = None
    # default Scrapy settings can be overridden via  custom_settings property
    # see https://docs.scrapy.org/en/latest/topics/settings.html for list of available settings
    custom_settings = {
        'CONCURRENT_REQUESTS': 128,
        # 'SPIDER_MIDDLEWARES':
        #     {'crawl_tools.crawler_scrapy.middlewares.SpiderMiddleware': 543}
    }

    def __init__(self, name=None, session=None, item=None, page=None, size=None, **kwargs):
        """

        :param name: name of spider to run
        :param session: session id (session_id)
        :param item: single item url (item_url)
        :param page: indicate which page must be processed in current session
        :param size: number of item that must be processed in current session
        Note: page and size parameters are useful when user wants to run
        multiple instances of one spider simultaneously(in the interest of time),
        each of which is responsible of processing a chunk of data
        The chunk that must be processed by current spider instance, is calculated
        with `page` and `size` parameters (see __slice method)
        """
        self.item_url = item
        self.page = int(page) if page is not None else None
        self.http = HttpHelper()
        self.session_id = str(session) if session is not None else Session.instance().session_id
        self.bulk_size = int(size) if size is not None else self.get_default_bulk_size()
        self.body = None
        super().__init__(name, **kwargs)

    def start_requests(self):
        """
        this method is called by Scrapy engine, therefore it's name should not be changed
        """
        if self.item_url is not None:
            yield scrapy.Request(url=self.item_url, callback=self.parse)
        elif self.sitemap_url is not None:
            yield scrapy.Request(url=self.sitemap_url, callback=self.crawl_sitemap_callback)
        else:
            urls = self.get_urls()
            if urls:
                list = self.__slice(self.get_urls())
                if list is not None:
                    for url in list:
                        yield scrapy.Request(url=url, callback=self.parse)

    def crawl_sitemap_callback(self, response):
        body = response.body
        doctors_list = Selector(text=body).xpath('//loc')
        list = self.__slice(doctors_list)
        if list is None:
            for doctor in self.__slice(doctors_list):
                link = doctor.get().replace('<loc>', '').replace('</loc>', '')
                if self.should_crawl_item(link):
                    yield scrapy.Request(link, self.parse)

    def get_urls(self):
        return []

    def get_settings_object(self):
        return None

    def parse(self, response):
        body = Selector(text=response.body)
        item_url = response.request.url
        self.save(body, item_url)

    @abstractmethod
    def get_data_repositories(self)-> List[RepositoryBase]:
        pass

    @abstractmethod
    def save(self, body: Selector, item_url: str):
        pass

    @abstractmethod
    def get_default_bulk_size(self) -> int:
        pass

    @abstractmethod
    def should_crawl_item(self, item_url) -> bool:
        pass

    def __slice(self, array: list):
        if array is not None and len(array) > 0:
            if self.page is None:
                return array
            page_size = self.bulk_size
            start = page_size * self.page
            if start > len(array):
                return None
            _next = self.page + 1
            stop = page_size * _next
            return array[start:stop]
