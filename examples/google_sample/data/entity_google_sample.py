import datetime

from data.entity_base import EntityBase


class GoogleSampleEntity(EntityBase):

    def __init__(self, session_id: str, crawl_date: datetime, url: str, link_address: str, link_title:str):
        self.link_address = link_address
        self.link_title = link_title
        super().__init__(session_id, crawl_date, url)
