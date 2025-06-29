class Vehicle:
    def __init__(self, vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity):
        self.__vehicleID = vehicleID
        self.__make = make
        self.__model = model
        self.__year = year
        self.__dailyRate = dailyRate
        self.__status = status
        self.__passengerCapacity = passengerCapacity
        self.__engineCapacity = engineCapacity

    # Getters
    @property
    def vehicleID(self):
        return self.__vehicleID

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def dailyRate(self):
        return self.__dailyRate

    @property
    def status(self):
        return self.__status

    @property
    def passengerCapacity(self):
        return self.__passengerCapacity

    @property
    def engineCapacity(self):
        return self.__engineCapacity
