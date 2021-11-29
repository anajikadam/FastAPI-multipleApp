import pandas as pd
import datetime
from pymongo import MongoClient

# Connect to MongoDB
dburl = "mongodb+srv://{}:{}@cluster0.jaby5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format("anaji_161121", "")
client = MongoClient(dburl)

# Create Database
db = client.CountryWpeople

IndianColl = db['Indian']
d1 = IndianColl.find_one({'Name': 'Mahatma Gandhi'})