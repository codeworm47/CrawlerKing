from spider_runner_base import SpiderRunnerBase
from crawlers.digiteb.spiders.abstraction.spider_base_selenium import SpiderBase
# do not delete this !


class SeleniumSpiderSpiderRunner(SpiderRunnerBase):

    def run(self, spider_name: str = None, item_url: str = None):
        if spider_name is not None:
            spider_instance = eval(spider_name)
            if item_url is not None:
                spider_instance.crawl_details(item_url)
            else:
                spider_instance.crawl_list()
        else:
            spiders = [cls() for cls in SpiderBase.__subclasses__()]
            for spider in spiders:
                spider.crawl_list()

