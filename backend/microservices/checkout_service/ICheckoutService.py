from abc import ABC, abstractmethod

class ICheckoutService(ABC):
    @abstractmethod
    def testing(self):
        pass

    @abstractmethod
    def addOrder(self):
        pass