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

# ... (rest of the functions remain the same)

def main():
    while True:
        print("\nOptions:")
        print("1. Registration/Login")
        print("2. Add Driver")
        print("3. Update Driver")
        print("4. Delete Driver")
        print("5. Add Vehicle")
        print("6. Add Allocation")
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
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
