import mysql.connector
from dao.ICarLeaseRepository import ICarLeaseRepository
from entity.Vehicle import Vehicle
from entity.Customer import Customer
from entity.Lease import Lease
from entity.Payment import Payment
from exception.CarNotFoundException import CarNotFoundException
from exception.CustomerNotFoundException import CustomerNotFoundException
from util.DBConnection import DBConnection

class ICarLeaseRepositoryImpl(ICarLeaseRepository):
    def __init__(self):
        self.connection = DBConnection.get_connection('config.properties')
        self.cursor = self.connection.cursor()

    def addCar(self, car: Vehicle):
        query = "INSERT INTO Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (car.make, car.model, car.year, car.dailyRate, car.status, car.passengerCapacity, car.engineCapacity))
        self.connection.commit()

    def removeCar(self, carID: int):
        query = "DELETE FROM Vehicle WHERE vehicleID = %s"
        self.cursor.execute(query, (carID,))
        self.connection.commit()

    def listAvailableCars(self):
        query = "SELECT * FROM Vehicle WHERE status = 'available'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def listRentedCars(self):
        query = "SELECT * FROM Vehicle WHERE status = 'notAvailable'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def findCarById(self, carID: int):
        query = "SELECT * FROM Vehicle WHERE vehicleID = %s"
        self.cursor.execute(query, (carID,))
        car = self.cursor.fetchone()
        if not car:
            raise CarNotFoundException(f"Car with ID {carID} not found")
        return car

    def addCustomer(self, customer: Customer):
        query = "INSERT INTO Customer (firstName, lastName, email, phoneNumber) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (customer.firstName, customer.lastName, customer.email, customer.phoneNumber))
        self.connection.commit()

    def removeCustomer(self, customerID: int):
        query = "DELETE FROM Customer WHERE customerID = %s"
        self.cursor.execute(query, (customerID,))
        self.connection.commit()

    def listCustomers(self):
        query = "SELECT * FROM Customer"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def findCustomerById(self, customerID: int):
        query = "SELECT * FROM Customer WHERE customerID = %s"
        self.cursor.execute(query, (customerID,))
        customer = self.cursor.fetchone()
        if not customer:
            raise CustomerNotFoundException(f"Customer with ID {customerID} not found")
        return customer

    def findLeaseById(self, leaseID: int):
        query = "SELECT * FROM Lease WHERE leaseID = %s"
        self.cursor.execute(query, (leaseID,))
        result = self.cursor.fetchone()
        
        if result:
            # Assuming the Lease class constructor takes these parameters
            return Lease(result[0], result[1], result[2], result[3], result[4], result[5])  # Adjust indices based on your Lease class
        else:
            return None  # Return None if no lease is found

    def createLease(self, customerID: int, carID: int, startDate, endDate, lease_type: str = "Daily"):
        # Validate the lease type
        if lease_type not in ['Daily', 'Monthly']:
            raise ValueError("Invalid lease type. Must be 'Daily' or 'Monthly'.")

        # Prepare the SQL query
        query = "INSERT INTO Lease (vehicleID, customerID, startDate, endDate, type) VALUES (%s, %s, %s, %s, %s)"
       
        # Execute the query
        self.cursor.execute(query, (carID, customerID, startDate, endDate, lease_type))
       
        # Commit the transaction
        self.connection.commit()
       
        # Return a Lease object with the last inserted ID
        return Lease(self.cursor.lastrowid, carID, customerID, startDate, endDate, lease_type)

    def returnCar(self, leaseID: int):
        query = "DELETE FROM Lease WHERE leaseID = %s"
        self.cursor.execute(query, (leaseID,))
        self.connection.commit()

    def listActiveLeases(self):
        query = "SELECT * FROM Lease"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def listLeaseHistory(self):
        query = "SELECT * FROM Lease"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def recordPayment(self, lease: Lease, amount: float):
        query = "INSERT INTO Payment (leaseID, paymentDate, amount) VALUES (%s, NOW(), %s)"
        self.cursor.execute(query, (lease.leaseID, amount))
        self.connection.commit()
