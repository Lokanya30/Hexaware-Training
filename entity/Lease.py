class Lease:
    def __init__(self, leaseID, vehicleID, customerID, startDate, endDate, leaseType):
        self.__leaseID = leaseID
        self.__vehicleID = vehicleID
        self.__customerID = customerID
        self.__startDate = startDate
        self.__endDate = endDate
        self.__leaseType = leaseType

    # Getters
    @property
    def leaseID(self):
        return self.__leaseID

    @property
    def vehicleID(self):
        return self.__vehicleID

    @property
    def customerID(self):
        return self.__customerID

    @property
    def startDate(self):
        return self.__startDate

    @property
    def endDate(self):
        return self.__endDate

    @property
    def leaseType(self):
        return self.__leaseType
