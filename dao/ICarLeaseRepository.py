from abc import ABC, abstractmethod
from entity.Vehicle import Vehicle
from entity.Customer import Customer
from entity.Lease import Lease

class ICarLeaseRepository(ABC):
    @abstractmethod
    def addCar(self, car: Vehicle):
        pass

    @abstractmethod
    def removeCar(self, carID: int):
        pass

    @abstractmethod
    def listAvailableCars(self):
        pass

    @abstractmethod
    def listRentedCars(self):
        pass

    @abstractmethod
    def findCarById(self, carID: int):
        pass

    @abstractmethod
    def addCustomer(self, customer: Customer):
        pass

    @abstractmethod
    def removeCustomer(self, customerID: int):
        pass

    @abstractmethod
    def listCustomers(self):
        pass

    @abstractmethod
    def findCustomerById(self, customerID: int):
        pass

    @abstractmethod
    def createLease(self, customerID: int, carID: int, startDate, endDate):
        pass

    @abstractmethod
    def returnCar(self, leaseID: int):
        pass

    @abstractmethod
    def listActiveLeases(self):
        pass

    @abstractmethod
    def listLeaseHistory(self):
        pass

    @abstractmethod
    def recordPayment(self, lease, amount):
        pass
