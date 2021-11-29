from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database.people import (
    retrieve_people,
    retrieve_peoples,
)


from app.server.models.people import (
    ErrorResponseModel,
    ResponseModel,
    PeopleSchema,
    UpdatePeopleModel,
)

router2 = APIRouter()


@router2.get("/", response_description="peoples retrieved")
async def get_peoples():
    peoples = await retrieve_peoples()
    if peoples:
        return ResponseModel(peoples, "peoples data retrieved successfully")
    return ResponseModel(peoples, "Empty list returned")


@router2.get("/{id}", response_description="people data retrieved")
async def get_people_data(id):
    people = await retrieve_people(id)
    if people:
        return ResponseModel(people, "people data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "people doesn't exist.")

###################

# http://127.0.0.1:8000/people/GetpeopleCount/country/country1
@router2.get("/GetpeopleCount/country/{countryName}", response_description="peoples retrieved")
async def get_peoples_count(countryName: str):
    from app.server.database.people import getListCollection, countPeoples
    collList = getListCollection()
    collListUpper = [i.upper() for i in collList]
    if countryName.upper() in collListUpper:
        count = countPeoples(countryName)
        return ResponseModel("Country Collection name {} has {} record".format(countryName, count),
                             "show count for given country successfully"
                             )
    return ErrorResponseModel(
        "An error occurred", 404, "Given country Name doesn't exist in Database"
    )


# http://127.0.0.1:8000/people/GetCountryList/ALL
@router2.get("/GetCountryList/{cnt}" )
async def get_GetCountryList_count(cnt: str):
    from app.server.database.people import GetCountryList
    dict11 = GetCountryList()
    return ResponseModel(
            dict11, "Get {} Country List with record count".format(cnt)
        )


# http://127.0.0.1:8000/people/country/USA   Get peoples data with country
@router2.get("/country/{countryname}", response_description="peoples retrieved")
async def get_peoples_country(countryname: str):
    from app.server.database.people import retrieve_peoples_country
    peoples = retrieve_peoples_country(countryname)
    if peoples:
        return ResponseModel(peoples, "peoples data retrieved successfully")
    return ResponseModel(peoples, "Empty list returned")

# http://127.0.0.1:8000/people/country/USA/count=10  Get peoples data with country
@router2.get("/country/{countryname}/count={count}", response_description="peoples retrieved")
async def get_peoples_country(countryname: str, count: int =10):
    from app.server.database.people import retrieve_peoples_country_cnt
    peoples = retrieve_peoples_country_cnt(countryname, count)
    # peoples = {k: peoples[k] for k, _ in zip(peoples, range(count))}
    if peoples:
        return ResponseModel(peoples, "peoples data retrieved successfully")
    return ResponseModel(peoples, "Empty list returned")

