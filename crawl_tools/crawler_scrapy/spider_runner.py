import os
from spider_runner_base import SpiderRunnerBase
from crawlers.digiteb.spiders.abstraction.spider_base_scrapy import SpiderBase
from scrapy import cmdline
# ! Do not delete this !
from crawlers.digiteb.spiders.spider_drdr_scrapy import DrdrSpider

"""
This class is in charge of creating and executing Scrapy spider(s) run command.
Note: this class only executes commands and the command is created correctly,
Scrpay itself instantiate the corresponding spider class and pass parameters as arguments
to spider's class constructor (see spider_base.py for more details)   
"""


class ScrapySpiderRunner(SpiderRunnerBase):

    def run(self, spider_name: str = None, params: dict = None):
        """
        create and execute a specific Scrapy spider or all the scrpy spiders(default) command(s) via Scrapy Cli.
        running mechanism works through Scrapy Cli. An execution command is prepared and generated
        via __get_spider_execution_command_by_type method and then passed to __execute_command method
        which is responsible of running commands in console
        :param spider_name: str
                            name of spider class which user desires to run
        :param params: list[dic]
                       run paramters as list of key/value pairs
        """
        if spider_name is not None:
            # run specific Scrapy spider
            spider_instance = eval(spider_name)
            command = self.__get_spider_execution_command_by_type(type(spider_instance), params)
            self.__execute_command(command)
        else:
            # run all the Scrapy spiders
            spiders = [cls() for cls in SpiderBase.__subclasses__()]
            for spider in spiders:
                command = self.__get_spider_execution_command_by_type(type(spider), params)
                self.__execute_command(command)

    def __get_spider_execution_command_by_type(self, spider_instance: type, params: dict = None):
        command = f'crawler_scrapy runspider {self._get_spider_file_path_by_type(type(spider_instance))}'
        if params is not None and len(params) > 0:
            for p in params:
                command += f' -a {p["key"]}={p["value"]}'
        return command

    @staticmethod
    def _get_spider_file_path_by_type(spider_instance: type)-> str:
        base_path = os.getcwd()
        file = f'{str(spider_instance.__module__).replace("." ,"/")}.py'
        return os.path.join(base_path, file)

    @staticmethod
    def __execute_command(command):
        """
        execute command in console using scrapy console helper (cmdline)
        """
        if command:
            cmdline.execute(command.split())

