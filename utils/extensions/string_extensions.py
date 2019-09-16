import random
import string
"""
This class contains set of helper(static) methods that extend behaviours to `str` class  
"""


class StringExtensions:

    @staticmethod
    def random(length: int) -> str:
        """
        returns a n characters lower-case randomized string
        :param length: int
        :return: str
        """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
