"""
This is a helper class for parsing of user-provided arguments
Note: I could use 'argeparse' package for this purpose, but since CrawlerKing argument parser logic is so simple and
wanted to pass arguments as a dictionary of key/value, decided to write this tiny parse
"""


class ArgHelper:
    @staticmethod
    def get_parameter_value(key: str, array: list) -> object:
        """
            find a value of specified key in an array of arguments

            Parameters
            ----------
            key: str
                 key to find
            array : list
                    array to search in
            Returns
            -------
            str :  value of specified key
        """
        if array is None or len(array) == 0:
            raise Exception('input array cannot be empty!')
        if key in array:
            key_index = array.index(key)
            value_index = key_index + 1
            if value_index > len(array):
                raise Exception(f'invalid array size'
                                f'a value must be provided for parameter {key}')
            return array[key_index + 1]
        return None

    @staticmethod
    def append_all_parameters(array: list) -> list:
        """
            parse and returns all parameters along with their values

            Parameters
            ----------
            array: list
                 list of parameters
            Returns
            -------
            list[dict] : returns all parsed parameters value as a list of dictionaries.
                        e.g [{'key':'page', 'value': '1'}]
        """
        list = []
        if len(array) > 0:
            for item in array:
                if str(item).startswith('--'):
                    value = ArgHelper.get_parameter_value(item, array)
                    if value is not None:
                        list.append({'key': ArgHelper.__normalize_key(item), 'value': value})
        return list

    @staticmethod
    def __normalize_key(key: str):
        return str(key).replace('--', '').replace('-', '_')
