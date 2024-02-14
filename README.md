# Project Name: FLEET MANAGEMENT SYSTEM
 
INTRODUCTION
Management of vehicles as a critical assest in many organizations is and has always been a major problem. Most of the time drivers allocated company vehicles do run personal or unauthorized trips with the vehicles allocated to them.Fuel costs are amoajor expenditure and repairs too.
 
PROBLEM STATEMENT
Most companies run manual fleet management systems for example government vehicles have manual work ticketing and outsourced repairs but no digital  tracking of vehicles data.
My project aims at the governmental side of tracking drivers,vehicles use and fuel consumption so as to indentify unique patterns from the database to be created using python Sqlalechmy.
A many to many relationship model of the fleet management where:_
A driver can be allocated vehicle

OBJECTIVES
This project aims to provide a functional digital the database to be created using python Sqlalechmy with these objectives:
  .Track drivers usage of the vehicle allocated
•	Reduce and curb  high vmisuse of vehicle
•	Reduce costs of operations by monitoring fule consumption
•	Protcet organizational assests(the vehicles)
•	Reward the drivers with great records
•	Track which vehicle brand is long lasting for future purchases.
 
ITS MVP/FEATURES:-
Airbnb Simple Application.
1. To have a dbdiagram and project structure.

2.	 Have the model.py,seed.py,debug.py
3.	Give the different type of vehicle,its brand, registration number and drivers when queried.
	
4.	Give the amount of fuel used by a vehicle 

5.	The data of allocation of vehicle to a driver for tarcking 


## Table of Contents

-Project’s  Description
- #installation to used for the project
run pipenv install && pipenv shell
alembic upgrade head
python seed.py
python debug.py
alembic revision -m "commit statements"
[License](#license)


## Description
This is a simple backend application that uses database information to the user when quiried for decision making especially in the transport sector.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies using run pipenv install && pipenv shell

## Contributing

Contributions are welcome. Please fork the repository and create a pull request for any proposed changes.

## License

This project is licensed under the :-
a. https://github.com/JEREMY-MK89/FLEET-MANAGEMENT-CLI

LANGUAGES TO BE USED
Back-End Interface: Sqlalchemy-SQLITE







Appendices
 


Its code 
CREATE TABLE `Allocation` (
  `id` Integer PRIMARY KEY,
  `driver_id` Integer NOT NULL,
  `vehicle_id` Integer NOT NULL,
  `allocation_date` Date NOT NULL,
  `fuel_amount` Float NOT NULL,
  `driver` Driver,
  `vehicle` Vehicle
);

CREATE TABLE `Driver` (
  `id` Integer PRIMARY KEY,
  `name` String NOT NULL,
  `allocations` Allocation
);

CREATE TABLE `Vehicle` (
  `id` Integer PRIMARY KEY,
  `type` String NOT NULL,
  `brand` String NOT NULL,
  `model` String NOT NULL,
  `registration_number` String NOT NULL,
  `allocations` Allocation
);

ALTER TABLE `Allocation` ADD FOREIGN KEY (`driver`) REFERENCES `Driver` (`allocations`);

ALTER TABLE `Allocation` ADD FOREIGN KEY (`vehicle`) REFERENCES `Vehicle` (`allocations`);

ALTER TABLE `Allocation` ADD FOREIGN KEY (`driver_id`) REFERENCES `Driver` (`id`);

ALTER TABLE `Allocation` ADD FOREIGN KEY (`vehicle_id`) REFERENCES `Vehicle` (`id`);

ALTER TABLE `Allocation` ADD FOREIGN KEY (`driver_id`) REFERENCES `Driver` (`allocations`);

ALTER TABLE `Allocation` ADD FOREIGN KEY (`vehicle_id`) REFERENCES `Vehicle` (`allocations`);


PROJCET STRUCTURE

/root/projectphase3/
|-- MY_LIB
|   |-- db
|   |   |-- (fleet_management.db-related files)
|   |-- migrations
|   |   |-- versions
|   |   |-- env.py
|   |   |-- README
|   |   |-- alembic.ini
|   |-- debug.py
|   |-- models.py
|   |-- seed.py
|-- .gitignore
