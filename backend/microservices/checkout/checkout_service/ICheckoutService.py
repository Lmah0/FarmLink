from abc import ABC, abstractmethod

class ICheckoutService(ABC):
    @abstractmethod
    def addOrder(self):
        pass