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
            data["locations"],
            data["deliveries"],
        )
        delivery.insert()

def initializeDb():
    addLocationData()
    addDeliveryData()
    addClientData()

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
    "pickups": [],
    "dropoffs": [],
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
    "pickups": [],
    "dropoffs": [], 
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
    "pickups": [],
    "dropoffs": [],  
}]

Delivery_default_data = [
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
        "dropoff_location_id": 2
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
        "dropoff_location_id": 1
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
        "dropoff_location_id": 1
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