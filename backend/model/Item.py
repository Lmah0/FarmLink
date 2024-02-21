class Item:
    def __init__(self, itemId, name, price, description, itemType, postingId):
        self.__itemId = itemId
        self.__name = name
        self.__price = price
        self.__description = description
        self.__itemType = itemType
        self.__postingId = postingId

    def __str__(self):
        return f"Item({self.itemId}, {self.name}, {self.price}, {self.description}, {self.itemType}, {self.postingId})"

    def to_dict(self):
        return {
            "itemId": self.itemId,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "itemType": self.itemType,
            "postingId": self.postingId
        }

    @staticmethod
    def from_dict(data):
        return Item(data["itemId"], data["name"], data["price"], data["description"], data["itemType"], data["postingId"])