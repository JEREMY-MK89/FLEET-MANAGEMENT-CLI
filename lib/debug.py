from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Driver, Vehicle, Allocation

def print_model_data(session, model_class, fields):
    print(f"\n{model_class.__name__}:")
    for instance in session.query(model_class).all():
        import ipdb; ipdb.set_trace()
        print(', '.join([f"{field}: {getattr(instance, field)}" for field in fields]))

def print_data():
    engine = create_engine('sqlite:///fleet_management.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    #  data to be printed from the tables
    print_model_data(session, Driver, ['id', 'name', 'vehicles'])
    print_model_data(session, Vehicle, ['id', 'type', 'brand', 'model', 'registration_number', 'drivers'])
    print_model_data(session, Allocation, ['id', 'driver_id', 'vehicle_id', 'allocation_date', 'fuel_amount'])

    print("\nAllocations:")
    for allocation in session.query(Allocation).all():
        import ipdb; ipdb.set_trace()
        print(f"Allocation ID: {allocation.id}")
        print(f"Driver ID: {allocation.driver_id}")
        print(f"Vehicle ID: {allocation.vehicle_id}")
        print(f"Allocation Date: {allocation.allocation_date}")
        print(f"Fuel Used: {allocation.fuel_amount}")
        # To Retrieve the vehicle details
        vehicle = session.query(Vehicle).get(allocation.vehicle_id)
        print(f"Vehicle Details: {vehicle.type} {vehicle.brand} {vehicle.model} ({vehicle.registration_number})")

if __name__ == '__main__':
    print_data()
