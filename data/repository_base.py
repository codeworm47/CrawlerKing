from abc import abstractmethod
from data.entity_base import EntityBase


class RepositoryBase:
    @abstractmethod
    def save(self, entity: EntityBase, options: dict = None):
        pass
