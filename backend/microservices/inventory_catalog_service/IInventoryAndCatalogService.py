from abc import ABC, abstractmethod

class IInventoryAndCatalogService(ABC):
    @abstractmethod
    def testing(self):
        pass

    @abstractmethod
    def addPosting(self):
        pass

