from opencage.geocoder import OpenCageGeocode
from utils.services.reverse_geo.reverse_geo_service_base import ReverseGeoServiceBase


"""
`OpenCage` Reverse Geo service implementation
documentation url : https://opencagedata.com/api
`opencage` package url : https://pypi.org/project/opencage/
"""


class OpenCageReverseGeoService(ReverseGeoServiceBase):

    def __init__(self, key: str):
        self.key = key

    def get_area_name_from_coordinates(self, lat: float, long: float) -> str:
        geocoder = OpenCageGeocode(self.key)
        res = geocoder.reverse_geocode(lat, long)
        return res[0]['components']['road']

    def get_city_name_from_coordinates(self, lat: float, long: float) -> str:
        geocoder = OpenCageGeocode(self.key)
        res = geocoder.reverse_geocode(lat, long)
        return res[0]['components']['city']
