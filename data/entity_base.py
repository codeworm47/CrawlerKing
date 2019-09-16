import datetime


class EntityBase:
    def __init__(self, session_id: str, crawl_date: datetime, url: str):
        self.session_id = session_id
        self.crawl_date = crawl_date
        self.url = url
