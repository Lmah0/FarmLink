from abc import ABC, abstractmethod

class IUserManagementService(ABC):
    @abstractmethod
    def testing(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def returnProfile(self):
        pass