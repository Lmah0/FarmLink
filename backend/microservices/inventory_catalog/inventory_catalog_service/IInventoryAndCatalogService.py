from abc import ABC, abstractmethod

class IInventoryAndCatalogService(ABC):
    @abstractmethod
    def addPosting(self):
        pass

    @abstractmethod
    def getPostings(self):
        pass

    @abstractmethod
    def getPosting(self):
        pass