from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Driver, Vehicle, Allocation

engine = create_engine('sqlite:///fleet_management.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def registration():
    print("Registration:")
    print("1. Sign Up")
    print("2. Proceed to Login")

    choice = input("Enter your choice: ")

    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    else:
        print("Invalid choice. Please try again.")

def sign_up():
    name = input("Enter driver's name: ")
    personal_number = input("Enter personal number: ")
    court_division = input("Enter court division: ")
    email = input("Enter email address: ")

    driver = Driver(name=name, personal_number=personal_number, court_division=court_division, email=email)
    session.add(driver)
    session.commit()
    print(f'Driver {name} signed up successfully!')

def login():
    email = input("Enter email address: ")
    personal_number = input("Enter personal number: ")

    driver = session.query(Driver).filter_by(email=email, personal_number=personal_number).first()

    if driver:
        print("Login successful!")
        # Add logic to proceed with the application after successful login
    else:
        print("Login failed. Please check your credentials.")

def add_driver():
    name = input("Enter driver's name: ")
    personal_number = input("Enter personal number: ")
    court_division = input("Enter court division: ")
    email = input("Enter email address: ")

    driver = Driver(name=name, personal_number=personal_number, court_division=court_division, email=email)
    session.add(driver)
    session.commit()
    print(f'Driver {name} added successfully!')

def update_driver():
    driver_id = int(input("Enter driver's ID to update: "))
    driver = session.query(Driver).filter_by(id=driver_id).first()

    if driver:
        print("Current Driver Details:")
        print(f"Name: {driver.name}")
        print(f"Personal Number: {driver.personal_number}")
        print(f"Court Division: {driver.court_division}")
        print(f"Email: {driver.email}")

        # Get updated details
        new_name = input("Enter new name (press Enter to keep current): ")
        new_personal_number = input("Enter new personal number (press Enter to keep current): ")
        new_court_division = input("Enter new court division (press Enter to keep current): ")
        new_email = input("Enter new email address (press Enter to keep current): ")

        # Update driver details
        if new_name:
            driver.name = new_name
        if new_personal_number:
            driver.personal_number = new_personal_number
        if new_court_division:
            driver.court_division = new_court_division
        if new_email:
            driver.email = new_email

        session.commit()
        print("Driver updated successfully!")
    else:
        print(f"Driver with ID {driver_id} not found.")

def delete_driver():
    driver_id = int(input("Enter driver's ID to delete: "))
    driver = session.query(Driver).filter_by(id=driver_id).first()

    if driver:
        session.delete(driver)
        session.commit()
        print("Driver deleted successfully!")
    else:
        print(f"Driver with ID {driver_id} not found.")

def add_vehicle():
    vehicle_type = input("Enter vehicle type: ")
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    registration_number = input("Enter registration number: ")

    # Assuming you have a drivers table and you want to associate drivers with this vehicle
    driver_ids_str = input("Enter driver IDs (comma-separated): ")
    driver_ids = [int(driver_id.strip()) for driver_id in driver_ids_str.split(",")]

    # Query drivers based on provided IDs
    drivers = session.query(Driver).filter(Driver.id.in_(driver_ids)).all()

    if not drivers:
        print("No drivers found for the provided IDs. Please make sure the drivers exist.")
        return

    vehicle = Vehicle(
        type=vehicle_type,
        brand=brand,
        model=model,
        registration_number=registration_number,
        drivers=drivers
    )

    session.add(vehicle)
    session.commit()
    print(f'Vehicle {brand} {model} added successfully!')

def list_drivers():
    drivers = session.query(Driver).all()
    print("\nList of Drivers:")
    for driver in drivers:
        print(f"ID: {driver.id}, Name: {driver.name}, Personal Number: {driver.personal_number}, "
              f"Court Division: {driver.court_division}, Email: {driver.email}")

def list_vehicles():
    vehicles = session.query(Vehicle).all()
    print("\nList of Vehicles:")
    for vehicle in vehicles:
        print(f"ID: {vehicle.id}, Type: {vehicle.type}, Brand: {vehicle.brand}, "
              f"Model: {vehicle.model}, Registration Number: {vehicle.registration_number}")



def main():
    while True:
        print("\nOptions:")
        print("1. Registration/Login")
        print("2. Add Driver")
        print("3. Update Driver")
        print("4. Delete Driver")
        print("5. Add Vehicle")
        print("6. Add Allocation")
        print("7. List Drivers")
        print("8. List Vehicles")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            registration()
        elif choice == "2":
            add_driver()
        elif choice == "3":
            update_driver()
        elif choice == "4":
            delete_driver()
        elif choice == "5":
            add_vehicle()
        elif choice == "6":
            add_allocation()
        elif choice == "7":
            list_drivers()
        elif choice == "8":
            list_vehicles()
        elif choice == "0":
            print("Exited successfully! Bye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
