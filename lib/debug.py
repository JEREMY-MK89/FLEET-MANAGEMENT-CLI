from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Driver, Vehicle, Allocation

def print_data():
    engine = create_engine('sqlite:///fleet_management.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Print data from the tables
    print("Drivers:")
    for driver in session.query(Driver).all():
        print(driver.id, driver.name, [vehicle.id for vehicle in driver.vehicles])

    print("\nVehicles:")
    for vehicle in session.query(Vehicle).all():
        print(vehicle.id, vehicle.type, vehicle.brand, vehicle.model, vehicle.registration_number, [driver.id for driver in vehicle.drivers])

    print("\nAllocations:")
    for allocation in session.query(Allocation).all():
        print(allocation.id, allocation.driver_id, allocation.vehicle_id, allocation.allocation_date, allocation.fuel_amount)

if __name__ == '__main__':
    print_data()
