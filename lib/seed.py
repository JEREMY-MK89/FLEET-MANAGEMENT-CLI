from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Driver, Vehicle, Allocation

# Create engine and bind metadata
engine = create_engine('sqlite:///fleet_management.db')

def seed_data():
    Session = sessionmaker(bind=engine)
    session = Session()

    # Sample data for allocations
    sample_allocations = [
        {"driver_id": 1, "vehicle_id": 1, "allocation_date": datetime.strptime("2024-02-15", "%Y-%m-%d"), "fuel_amount": 30.5},
        {"driver_id": 2, "vehicle_id": 2, "allocation_date": datetime.strptime("2024-02-16", "%Y-%m-%d"), "fuel_amount": 50.0},
        {"driver_id": 3, "vehicle_id": 3, "allocation_date": datetime.strptime("2024-02-17", "%Y-%m-%d"), "fuel_amount": 100.0},
        {"driver_id": 4, "vehicle_id": 4, "allocation_date": datetime.strptime("2024-02-19", "%Y-%m-%d"), "fuel_amount": 250.0},
    ]

    # Populate allocations table with sample data
    for allocation_data in sample_allocations:
        allocation = Allocation(**allocation_data)
        session.add(allocation)

    # Sample data for drivers
    sample_drivers = [
        {"name": "Muthengi Muthami", "personal_number": "001", "court_division": "Nairobi", "email": "muthengi@example.com", "vehicles": [1]},
        {"name": "Charles Kirui", "personal_number": "002", "court_division": "Mombasa", "email": "charles@example.com", "vehicles": [2]},
        {"name": "John Munene", "personal_number": "003", "court_division": "Kisumu", "email": "john@example.com", "vehicles": [3]},
        {"name": "Rashid Ali Smith", "personal_number": "004", "court_division": "Nakuru", "email": "rashid@example.com", "vehicles": [4]},
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
        {"type": "Truck", "brand": "Isuzu", "model": "N-Series", "registration_number": "GHI789", "drivers": [3]},
        {"type": "Bus", "brand": "Scania", "model": "K-Series", "registration_number": "JKL012", "drivers": [4]},
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
    # Create tables before seeding data
    Base.metadata.create_all(engine)
    # Seed the data
    seed_data()
