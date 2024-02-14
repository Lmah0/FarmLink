class User:
    def __init__(self, name, userId, phoneNumber, emailAddresss, password, role, profileBio):
        self.__name = name
        self.__userId = userId
        self.__phoneNumber = phoneNumber
        self.__emailAddresss = emailAddresss
        self.__password = password
        self.__role = role
        self.__farmerPid = None
        self.__postings = []
        self.__orders = []
        self.__creditCardNumber = None
        self.__profileBio = profileBio