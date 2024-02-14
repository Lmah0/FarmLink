class Order:
    def __init__(self, orderId, userId, items, purchaseDate, totalCost):
        self.__orderId = orderId
        self.__userId = userId
        self.__items = items
        self.__purchaseDate = purchaseDate
        self.__totalCost = totalCost
        self.__orderStatus = "Processing"