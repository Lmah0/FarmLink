class Item:
    def __init__(self, itemId, name, price, description, itemType):
        self.__itemId = itemId
        self.__name = name
        self.__rice = price
        self.__description = description
        self.__itemType = itemType

    def __str__(self):
        return f"Item({self.itemId}, {self.name}, {self.price}, {self.description}, {self.itemType})"

    def to_dict(self):
        return {
            "itemId": self.itemId,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "itemType": self.itemType
        }

    @staticmethod
    def from_dict(data):
        return Item(data["itemId"], data["name"], data["price"], data["description"], data["itemType"])