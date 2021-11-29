from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class CountrySchema(BaseModel):
    Country: str = Field(..., example="India")
    people_Count: int = Field(...)
    Link: str = Field(..., example="www.thefamouspeople.com/india.php")

    class Config:
        schema_extra = {
            "example": {
                "Country": "Indian",
                "people_Count": "3087",
                "Link": "//www.thefamouspeople.com/india.php",
            }
        }



class UpdateCountryModel(BaseModel):
    Country: str = Field(..., example="India")
    people_Count: int = Field(...)
    Link: str = Field(..., example="www.thefamouspeople.com/india.php")

    class Config:
        schema_extra = {
            "example": {
                "Country": "Indian",
                "people_Count": "3087",
                "Link": "//www.thefamouspeople.com/india.php",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}