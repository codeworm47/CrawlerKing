from spider_runner_base import SpiderRunnerBase
# ! Do not delete these !
import sys
from utils.helpers.arg_helper import ArgHelper
"""
This file is main entry point and is responsible of running spider(s).
This is actually CrawlerKing runner that decides which spider(s) must be run with what parameters
based on user-provided parameters.
If no parameter is provider (default behavior), it will run all the spiders of all kinds e.g Scrapy, Selenium etc

used is allowed to pass any number of parameters 
and runner must parse parameters and pass them to desired spider (if specified) or all the spiders 
The parameters must be given in GNU/POSIX convention, parameters name must begin with '--' 
and their value must be specified right next to them 
e.g --page 2
    --page 2 --verbose true
Note: runner doesn't support default value, because it's not much making sense in this case. For instance if user 
providers '--page' parameter they must specify what page they desire.    
"""

args = sys.argv
list = None
spider_name = None
if len(args) > 0:
    # removing name of file from args (run.py)
    args = args[1:len(args)]
    spider_name = ArgHelper.get_parameter_value('--spider', args)
    list = ArgHelper.append_all_parameters(args)

# retrieving all SpiderRunnerBase classes e.g ScrapySpiderRunner, SeleniumSpiderRunner
runners = [cls() for cls in SpiderRunnerBase.__subclasses__()]
for runner in runners:
    spider_given = spider_name is not None
    list_given = list is not None and len(list) > 0

    if spider_given and list_given:
        runner.run(spider_name, list)
    elif spider_given and not list_given:
        runner.run(spider_name=spider_name)
    elif not spider_given and list_given:
        runner.run(params=list)
    else:
        runner.run()




