class Customer:
    def __init__(self, customerID, firstName, lastName, email, phoneNumber):
        self.__customerID = customerID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__phoneNumber = phoneNumber

    # Getters
    @property
    def customerID(self):
        return self.__customerID

    @property
    def firstName(self):
        return self.__firstName

    @property
    def lastName(self):
        return self.__lastName

    @property
    def email(self):
        return self.__email

    @property
    def phoneNumber(self):
        return self.__phoneNumber
