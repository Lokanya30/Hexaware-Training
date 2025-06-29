import unittest
from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from entity.Customer import Customer
from entity.Vehicle import Vehicle
from myexceptions.CarNotFoundException import CarNotFoundException

class TestCarRental(unittest.TestCase):
    def setUp(self):
        self.repo = ICarLeaseRepositoryImpl()

    def test_add_customer(self):
        customer = Customer(None, "John", "Doe", "john@example.com", "1234567890")
        self.repo.addCustomer(customer)
        self.assertIsNotNone(self.repo.findCustomerById(1))  # Assuming ID 1 is the first customer

    def test_add_car(self):
        car = Vehicle(None, "Toyota", "Camry", 2022, 50.0, "available", 5, 2.5)
        self.repo.addCar(car)
        self.assertIsNotNone(self.repo.findCarById(1))  # Assuming ID 1 is the first car

    def test_find_car_not_found(self):
        with self.assertRaises(CarNotFoundException):
            self.repo.findCarById(9999)  # Assuming 9999 does not exist

if __name__ == '__main__':
    unittest.main()
