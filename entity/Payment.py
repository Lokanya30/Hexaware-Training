class Payment:
    def __init__(self, paymentID, leaseID, paymentDate, amount):
        self.__paymentID = paymentID
        self.__leaseID = leaseID
        self.__paymentDate = paymentDate
        self.__amount = amount

    # Getters
    @property
    def paymentID(self):
        return self.__paymentID

    @property
    def leaseID(self):
        return self.__leaseID

    @property
    def paymentDate(self):
        return self.__paymentDate

    @property
    def amount(self):
        return self.__amount
