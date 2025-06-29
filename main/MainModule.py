import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from entity.Customer import Customer
from entity.Vehicle import Vehicle
from entity.Lease import Lease
from exception.CarNotFoundException import CarNotFoundException
from exception.CustomerNotFoundException import CustomerNotFoundException

class MainModule:
    def __init__(self):
        self.repo = ICarLeaseRepositoryImpl()

    def run(self):
        while True:
            print("1. Add Customer")
            print("2. Add Car")
            print("3. Create Lease")
            print("4. Record Payment")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                customer = Customer(None, first_name, last_name, email, phone_number)
                self.repo.addCustomer(customer)
                print("Customer added successfully.")

            elif choice == '2':
                make = input("Enter car make: ")
                model = input("Enter car model: ")
                year = int(input("Enter car year: "))
                daily_rate = float(input("Enter daily rate: "))
                status = input("Enter status (available/notAvailable): ")
                passenger_capacity = int(input("Enter passenger capacity: "))
                engine_capacity = float(input("Enter engine capacity: "))
                car = Vehicle(None, make, model, year, daily_rate, status, passenger_capacity, engine_capacity)
                self.repo.addCar(car)
                print("Car added successfully.")

            elif choice == '3':
                customer_id = int(input("Enter customer ID: "))
                car_id = int(input("Enter car ID: "))
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                lease = self.repo.createLease(customer_id, car_id, start_date, end_date, "Daily") 
                print(f"Lease created successfully with ID: {lease.leaseID}")

            elif choice == '4':
                lease_id = int(input("Enter lease ID: "))
                amount = float(input("Enter payment amount: "))
                lease = self.repo.findLeaseById(lease_id)  # You need to implement this method
                self.repo.recordPayment(lease, amount)
                print("Payment recorded successfully.")

            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
