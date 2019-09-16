from abc import abstractmethod

"""
Every spider runner (such as scrpy spider runner, selenium spider runner and so on), is SpiderRunnerBase
and must implement its own run method properly
"""


class SpiderRunnerBase:
    @abstractmethod
    def run(self, spider_name: str = None, params: dict = None):
        pass
    """
        This method is responsible of running spider(s) of specific kind for instance Scrapy spider or selenium spider.
        If no argument is passed(default behavior), it will run all the spiders of that specific type.
        
        Parameters
        ----------
        spider_name: str
                     name of spider to run, if not given, all the spiders will be run.
        params: dict
                dictionary contains of key/value pairs e.g : [{'key':'page', 'value':2}]              
    """
