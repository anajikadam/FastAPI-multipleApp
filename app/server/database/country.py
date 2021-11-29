# import motor.motor_asyncio

from bson.objectid import ObjectId

from pymongo import MongoClient

from app.server.database.cred import MONGO_DETAILS
client = MongoClient(MONGO_DETAILS)

db = client.country
country_collection = db['country0']

def country_helper(country) -> dict:
    return {
        "id": str(country["_id"]),
        "Country": country["Country"],
        "people_Count": country["people_Count"],
        "Link": country["Link"],
    }

# Retrieve all Country present in the database
async def retrieve_countrys():
    countrys = []
    for country in country_collection.find():
        countrys.append(country_helper(country))
    return countrys

# Retrieve a Country with a matching ID
async def retrieve_country(id: str) -> dict:
    country = country_collection.find_one({"_id": ObjectId(id)})
    if country:
        return country_helper(country)


