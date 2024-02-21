class Order:
    def __init__(self, orderId, userId, purchaseDate, totalCost, orderedItems):
        self.__orderId = orderId
        self.__userId = userId
        self.__orderedItems = orderedItems
        self.__purchaseDate = purchaseDate
        self.__totalCost = totalCost
