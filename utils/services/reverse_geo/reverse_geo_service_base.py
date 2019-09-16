from abc import abstractmethod

"""
This class is a base for all Reverse Geo services.
Currently it has only two method but other methods will be added probably later 
"""


class ReverseGeoServiceBase:
    @abstractmethod
    def get_city_name_from_coordinates(self, lat: float, long: float) -> str:
        """
        returns a city name from specific latitude and longitude
        :param lat: latitude
        :param long: longitude
        :return: str
                 city name
        """
        pass

    @abstractmethod
    def get_area_name_from_coordinates(self, lat: float, long: float) -> str:
        """
        returns a city name from specific latitude and longitude
        :param lat: latitude
        :param long: longitude
        :return: str
                 city name
        """
        pass
