import os
from sqlalchemy import Column, String, Integer, DateTime, Boolean, create_engine, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "autoflow"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)



'''
Locations

'''


class Location(db.Model):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    location_name = Column(String)
    primary_location = Column(Boolean)
    primary_contact = Column(String)
    email = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    phone = Column(String)

    def __init__(
        self,
        location_name,
        primary_contact,
        email,
        address,
        city,
        state,
        zip_code,
        phone,
    ):
        self.location_name = location_name
        self.primary_contact = primary_contact
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        # self.pickups = pickups
        # self.dropoffs = dropoffs

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'company_name': self.company_name,
            'primary_contact': self.primary_contact,
            'email': self.email,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'phone': self.phone,
        }


'''
Delivery
'''


class Delivery(db.Model):
    __tablename__ = 'delivery'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    date_created = Column(DateTime)
    item = Column(String)
    notes = Column(String, nullable=True)
    date_fulfilled = Column(DateTime, nullable=True)
    pickup_location_id = Column(Integer, ForeignKey('location.id'))
    dropoff_location_id = Column(Integer, ForeignKey('location.id'))
    pickup_location = relationship("Location", foreign_keys=[pickup_location_id])
    dropoff_location = relationship("Location", foreign_keys=[dropoff_location_id])

    def __init__(
        self,
        client_id,
        date_created,
        item,
        notes,
        date_fulfilled,
        pickup_location_id,
        dropoff_location_id,
    ):
        self.client_id = client_id,
        self.date_created = date_created,
        self.item = item,
        self.notes = notes,
        self.date_fulfilled, date_fulfilled,
        self.pickup_location_id = pickup_location_id,
        self.dropoff_location_id = dropoff_location_id
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'role': self.role
        }
        
        
'''
Client

'''


class Client(db.Model):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    locations = relationship("Location")
    deliveries = relationship("Delivery")

    def __init__(self, name):
        self.name = name,
        # self.locations = locations
        # self.deliveries = deliveries

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # def format(self):
    #     return {
    #         'company_name': self.company_name,
    #         'primary_contact': self.primary_contact,
    #         'email': self.email,
    #         'address': self.address,
    #         'city': self.city,
    #         'state': self.state,
    #         'zip_code': self.zip_code,
    #         'phone': self.phone,
    #     }


# ---------------------------------------------------------------------------- #
# Initialize Database
# ---------------------------------------------------------------------------- #


def addLocationData():
    for data in location_default_data:
        location = Location(
            data["location_name"],
            data["primary_contact"],
            data["email"],
            data["address"],
            data["city"],
            data["state"],
            data["zip_code"],
            data["phone"],
        )
        location.insert()


def addDeliveryData():
    for data in delivery_default_data:
        delivery = Delivery(
            data["client_id"],
            data["date_created"],
            data["item"],
            data["notes"],
            data["date_fulfilled"],
            data["pickup_location_id"],
            data["dropoff_location_id"],
        )
        delivery.insert()
        
def addClientData():
    for data in client_default_data:
        client = Client(
            data["name"],
            # data["locations"],
            # data["deliveries"],
        )
        client.insert()

def initializeDb():
    addClientData()
    addLocationData()
    addDeliveryData()

# ---------------------------------------------------------------------------- #
# Initial App Data
# ---------------------------------------------------------------------------- #

location_default_data = [
{
    "client_id": 1,
    "location_name": "HQ",
    "primary_location": True,
    "primary_contact": "Jack Dorsey",
    "email": "jdorsey@twitter.com",
    "address": "1355 Market St #900",
    "city": "San Francisco",
    "state": "CA",
    "zip_code": "94103",
    "phone": "+14152229670",
    "pickups": [1,2],
    "dropoffs": [4,6],
},
{
    "client_id": 2,
    "location_name": "HQ",
    "primary_location": True,
    "primary_contact": "Elon Musk",
    "email": "emusk@tesla.com",
    "address": "3500 Deer Creek Rd",
    "city": "Palo Alto",
    "state": "CA",
    "zip_code": "94304",
    "phone": "+14152229670",
    "pickups": [3,4],
    "dropoffs": [1,2,5], 
},
{
    "client_id": 3,
    "location_name": "Campus",
    "primary_location": True,
    "primary_contact": "Jamie Parenteau",
    "email": "jparenteau@42.us.org",
    "address": "6600 Dumbarton Circle",
    "city": "Fremont",
    "state": "CA",
    "zip_code": "Fremont",
    "phone": "+14152229670",
    "pickups": [5,6],
    "dropoffs": [3],  
}]

delivery_default_data = [
    {
        "client_id": 1,
        "date_created": "2019-05-21T21:30:00.000Z",
        "item": "Mackbook Pro",
        "notes": "This is a gray 15\" model",
        "pickup_location_id": 1,
        "dropoff_location_id": 2,
        "date_fulfilled": "2019-05-21T21:30:00.000Z",
    },
    {
        "client_id": 1,
        "date_created": "2019-05-21T21:30:00.000Z",
        "item": "Lunch",
        "notes": "Its a PB & J sandwitch and an apple",
        "pickup_location_id": 1,
        "dropoff_location_id": 2,
        "date_fulfilled": None,
    },
    {
        "client_id": 2,
        "date_created": "2019-05-21T21:30:00.000Z",
        "item": "Intern",
        "notes": "Intern's name is Dan",
        "pickup_location_id": 2,
        "dropoff_location_id": 3,
        "date_fulfilled": "2019-05-21T21:30:00.000Z",
    },
    {
        "client_id": 2,
        "date_created": "2019-05-21T21:30:00.000Z",
        "item": "Lunch",
        "notes": "Its a steak dinner with a side of mac and cheese",
        "pickup_location_id": 2,
        "dropoff_location_id": 1,
        "date_fulfilled": None,
    },
    {
        "client_id": 3,
        "date_created": "2019-05-21T21:30:00.000Z",
        "item": "Autonomous RC car",
        "notes": "It's name is marvin",
        "pickup_location_id": 3,
        "dropoff_location_id": 2,
        "date_fulfilled": "2019-05-21T21:30:00.000Z",
    },
    {
        "client_id": 3,
        "date_created": "2019-05-21T21:30:00.000Z",
        "item": "Lunch",
        "notes": "It's ramen noodles",
        "pickup_location_id": 3,
        "dropoff_location_id": 1,
        "date_fulfilled": None,
    },
]


client_default_data= [
    {
        "name": "Twitter",
        "locations": [1],
        "deliveries": [1,2],
    },
    {
        "name": "Tesla",
        "locations": [2],
        "deliveries": [3,4],
    },
    {
        "name": "42 Silicon Valley",
        "locations": [3],
        "deliveries": [5,6],
    },
]

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    initializeDb()