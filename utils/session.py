from utils.extensions.string_extensions import StringExtensions

"""
This is Singleton class which hold information about current session
Currently it has only one property named session_id, but later it will be more mature 
"""


class Session:
    __instance = None

    @staticmethod
    def instance():
        """ Static access method. """
        if Session.__instance is None:
            Session()
        return Session.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Session.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Session.__instance = self
        self.session_id = StringExtensions.random(5)
