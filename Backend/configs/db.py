import os
from pymongo import MongoClient

import certifi  # Required to connect the Mongo DB atlas and run on MacOS

Mongo_link = os.getenv('MONGO_URI')

# Establish connection to MongoDB

# "tlsCAFile=certifi.where()" is required to add to establish connection and run on MacOS
client = MongoClient(Mongo_link, tlsCAFile=certifi.where())
db = client['EvenTix']


# Export the database connection
dbConnection = db
