import reverse_geocoder as rg
from utils.services.reverse_geo.reverse_geo_service_base import ReverseGeoServiceBase


"""
built-in python `ReverseGeoCoder` Reverse Geo service implementation
"""


class ReverseGeoCoderReverseGeoService(ReverseGeoServiceBase):

    def __init__(self, key: str):
        self.key = key

    def get_area_name_from_coordinates(self, lat: float, long: float) -> str:
        raise NotImplemented('Currently built-in python ReverseGeoCoder package does not support area name reversing')

    def get_city_name_from_coordinates(self, lat: float, long: float) -> str:
        res = rg.search((lat, long), mode=1)
        return res[0]['name']

