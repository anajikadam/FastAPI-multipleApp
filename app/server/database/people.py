# import motor.motor_asyncio
from pymongo import MongoClient

from bson.objectid import ObjectId

from app.server.database.cred import MONGO_DETAILS

client = MongoClient(MONGO_DETAILS)

db = client.CountryWpeople
people_collection = db['Indian']

# helpers


def people_helper(people) -> dict:
    return {
        "id": str(people["_id"]),
        "Number": people["Number"],
        "Name": people["Name"],
        "img_link": people["img_link"],
        "link": people["link"],
        "info": people["info"],
    }

# crud operations

# Retrieve all peoples present in the database
async def retrieve_peoples():
    peoples = []
    for people in people_collection.find():
        peoples.append(people_helper(people))
    return peoples


# Retrieve a people with a matching ID
async def retrieve_people(id: str) -> dict:
    people = people_collection.find_one({"_id": ObjectId(id)})
    if people:
        return people_helper(people)


def getListCollection():
    return db.list_collection_names()

# def deleteCountry(countryName):
#     coll = db11[str(countryName)] 
#     coll.drop()

def countPeoples(countryname):
    custom_collection = db[str(countryname)] 
    return custom_collection.count()

def GetCountryList():
    dict1 = {}
    for i in db.list_collection_names():
        dict1.update({i: db[i].count_documents({})})
    return dict1


# Retrieve all peoples present in the database
def retrieve_peoples_country(countryname):
    custom_collection = db[str(countryname)] 
    peoples = []
    for people in custom_collection.find():
        peoples.append(people_helper(people))
    return peoples

# Retrieve all peoples present in the database
def retrieve_peoples_country_cnt(countryname, count):
    custom_collection = db[str(countryname)] 
    peoples = []
    for people in custom_collection.find()[:count]:
        peoples.append(people_helper(people))
    return peoples