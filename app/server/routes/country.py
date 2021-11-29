from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database.country import (
    retrieve_country,
    retrieve_countrys,
)

from app.server.models.country import (
    ErrorResponseModel,
    ResponseModel,
    CountrySchema,
    UpdateCountryModel,
)

router1 = APIRouter()


@router1.get("/", response_description="countrys retrieved")
async def get_countrys():
    countrys = await retrieve_countrys()
    if countrys:
        return ResponseModel(countrys, "countrys data retrieved successfully")
    return ResponseModel(countrys, "Empty list returned")


@router1.get("/{id}", response_description="country data retrieved")
async def get_country_data(id):
    country = await retrieve_country(id)
    if country:
        return ResponseModel(country, "country data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "country doesn't exist.")

