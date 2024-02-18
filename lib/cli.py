from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Driver, Vehicle, Allocation  # Import your models

engine = create_engine('sqlite:///fleet_management.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_driver():
    name = input("Enter driver's name: ")
    driver = Driver(name=name)
    session.add(driver)
    session.commit()
    print(f'Driver {name} added successfully!')

def add_vehicle():
    type = input("Enter vehicle type: ")
    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    registration_number = input("Enter registration number: ")

    vehicle = Vehicle(type=type, brand=brand, model=model, registration_number=registration_number)
    session.add(vehicle)
    session.commit()
    print(f'Vehicle {brand} {model} added successfully!')

def add_allocation():
    driver_id = int(input("Enter driver ID: "))
    vehicle_id = int(input("Enter vehicle ID: "))
    allocation_date = input("Enter allocation date (YYYY-MM-DD): ")
    fuel_amount = float(input("Enter fuel amount: "))

    allocation = Allocation(driver_id=driver_id, vehicle_id=vehicle_id, allocation_date=allocation_date, fuel_amount=fuel_amount)
    session.add(allocation)
    session.commit()
    print(f'Allocation added successfully!')

def main():
    while True:
        print("\nOptions:")
        print("1. Add Driver")
        print("2. Add Vehicle")
        print("3. Add Allocation")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_driver()
        elif choice == "2":
            add_vehicle()
        elif choice == "3":
            add_allocation()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
