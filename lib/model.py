from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

association_table = Table('driver_vehicle_association', Base.metadata,
    Column('driver_id', Integer, ForeignKey('drivers.id')),
    Column('vehicle_id', Integer, ForeignKey('vehicles.id'))
)

class Allocation(Base):
    __tablename__ = 'allocations'
    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey('drivers.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    allocation_date = Column(Date, nullable=False)
    fuel_amount = Column(Float, nullable=False)
    driver = relationship('Driver', back_populates='allocations')
    vehicle = relationship('Vehicle', back_populates='allocations')

    def __repr__(self):
        return f'Allocation(id={self.id}, driver_id={self.driver_id}, vehicle_id={self.vehicle_id}, ' + \
               f'allocation_date={self.allocation_date}, fuel_amount={self.fuel_amount})'

class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    personal_number = Column(String, nullable=False, server_default='')  # Added this line
    court_division = Column(String, nullable=False, server_default='')  # Added this line
    email = Column(String, nullable=False, server_default='')  # Added this line
    allocations = relationship('Allocation', back_populates='driver')
    vehicles = relationship('Vehicle', secondary=association_table, back_populates='drivers')

    def __repr__(self):
        return f'Driver(id={self.id}, name={self.name}, personal_number={self.personal_number}, ' + \
               f'court_division={self.court_division}, email={self.email})'

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    registration_number = Column(String, nullable=False)
    allocations = relationship('Allocation', back_populates='vehicle')
    drivers = relationship('Driver', secondary=association_table, back_populates='vehicles')

    def __repr__(self):
        return f'Vehicle(id={self.id}, type={self.type}, brand={self.brand}, ' + \
               f'model={self.model}, registration_number={self.registration_number})'
