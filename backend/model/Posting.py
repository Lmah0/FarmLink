class Posting:
    def __init__(self, userId, postedItem, postingId, quantity, postingAuthor, description=None):
        self.__userId = userId
        self.__postedItem = postedItem
        self.__postingId = postingId
        self.__quantity = quantity
        self.__postingAuthor = postingAuthor
        self.__description = description