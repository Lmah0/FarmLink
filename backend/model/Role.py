from enum import Enum

class Role(Enum):
    FARMER = 0
    NONFARMER = 1
    
    def __str__(self):
        return self.name