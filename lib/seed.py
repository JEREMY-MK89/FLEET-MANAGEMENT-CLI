from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Driver, Vehicle, Allocation

def seed_data():
    engine = create_engine('sqlite:///fleet_management.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Sample data for allocations
    sample_allocations = [
        {"driver_id": 1, "vehicle_id": 1, "allocation_date": "2024-02-15", "fuel_amount": 30.5},
        {"driver_id": 2, "vehicle_id": 2, "allocation_date": "2024-02-16", "fuel_amount": 50.0},
        {"driver_id": 3, "vehicle_id": 3, "allocation_date": "2024-02-17", "fuel_amount": 100.0},
        {"driver_id": 4, "vehicle_id": 4, "allocation_date": "2024-02-19", "fuel_amount": 250.0},
    ]

    # Populate allocations table with sample data
    for allocation_data in sample_allocations:
        allocation = Allocation(**allocation_data)
        session.add(allocation)

    # Sample data for drivers
    sample_drivers = [
        {"name": "Muthengi muthami", "vehicles": [1]},
        {"name": "charles kirui", "vehicles": [2]},
        {"name": "John munene", "vehicles": [3]},
        {"name": "Rashid Ali Smith", "vehicles": [4]},
    ]

    # Populate drivers table with sample data
    for driver_data in sample_drivers:
        vehicles_ids = driver_data.pop("vehicles", [])
        driver = Driver(**driver_data)
        driver.vehicles = session.query(Vehicle).filter(Vehicle.id.in_(vehicles_ids)).all()
        session.add(driver)

    # Sample data for vehicles
    sample_vehicles = [
        {"type": "Car", "brand": "Toyota", "model": "Sedan", "registration_number": "ABC123", "drivers": [1]},
        {"type": "Van", "brand": "Ford", "model": "Heavy Duty", "registration_number": "DEF456", "drivers": [2]},
        {"type": "Truck", "brand": "Ford", "model": "Heavy Duty", "registration_number": "DEF456", "drivers": [3]},
        {"type": "Bus", "brand": "Ford", "model": "Heavy Duty", "registration_number": "DEF456", "drivers": [4]},
    ]

    # Populate vehicles table with sample data
    for vehicle_data in sample_vehicles:
        drivers_ids = vehicle_data.pop("drivers", [])
        vehicle = Vehicle(**vehicle_data)
        vehicle.drivers = session.query(Driver).filter(Driver.id.in_(drivers_ids)).all()
        session.add(vehicle)

    session.commit()
    print("Database seeded with sample data.")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    seed_data()
