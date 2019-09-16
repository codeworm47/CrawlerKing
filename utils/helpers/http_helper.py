import requests
import requests.adapters

"""
This is a small helper based on 'requests' package in order to making http requests easier for developers and 
integration and centralizing all the settings related to http request (such as base url, pool size, max pool size,
default headers and cookies and so on) in one place so that we could easily manipulate those setting later on.    
"""


class HttpHelper:

    def __init__(self, base_url: str = None, headers: dict = None, cookies: dict = None,
                 pool_size: int = 100, pool_max_size: int = 100):
        self.base_url = base_url
        sess = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=pool_size, pool_maxsize=pool_max_size)
        sess.mount('http://', adapter)
        sess.mount('https://', adapter)
        if headers is not None and len(headers) > 0:
            sess.headers = headers
        if cookies is not None and len(cookies) > 0:
            sess.cookies = cookies
        self.session = sess

    def get_json(self, url: str) -> dict:
        """
        calls a json-formatted api
        :param url: api url
        :return: dict
        """
        try:
            _url = url
            with self.session as sess:
                if self.base_url is not None:
                    _url = self.base_url + url
                response = sess.get(_url)
            return response.json()
        except requests.exceptions.RequestException as ex:
            print(url, ex)
            raise ex

    def get_raw_content(self, url: str) -> str:
        """
        make request to a url and return it's response intact (without any parsing or modification)
        :param url: url
        :return: str
                 url direct response as string
        """
        try:
            _url = url
            with self.session as sess:
                if self.base_url is not None:
                    _url = self.base_url + url
                response = sess.get(_url)
            return response.content
        except requests.exceptions.RequestException as ex:
            print(url, ex)
            raise ex


