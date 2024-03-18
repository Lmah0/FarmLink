from abc import ABC, abstractmethod

class IShoppingCartService(ABC):
    @abstractmethod
    def addToCart(self):
        pass

    @abstractmethod
    def removeFromCart(self):
        pass

    @abstractmethod
    def returnCart(self):
        pass

    @abstractmethod
    def flushCart(self):
        pass

