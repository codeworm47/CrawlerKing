"""
This class contains set of helper(static) methods that extend behaviours to `float` class
"""


class FloatExtensions:

    @staticmethod
    def is_float(val) -> bool:
        try:
            float(val)
            return True
        except ValueError:
            return False
