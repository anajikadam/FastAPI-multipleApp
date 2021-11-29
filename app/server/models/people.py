from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class PeopleSchema(BaseModel):
    Number: int = Field(...)
    Name: str = Field(...)
    img_link: str = Field(...)
    link: str = Field(...)
    info: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Number": "1",
                "Name": "Mahatma Gandhi",
                "img_link": "www.thefamouspeople.com/profiles/thumbs/mahatma-gandhi-36.jpg",
                "link": "www.thefamouspeople.com/profiles/mahatma-gandhi-55.php",
                "info": "['Listed In: Historical Personalities', ]",
            }
        }


class UpdatePeopleModel(BaseModel):
    Number: Optional[int]
    Name: Optional[str]
    img_link: Optional[str]
    link: Optional[str]
    info: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "Number": "1*",
                "Name": "Mahatma Gandhi",
                "img_link": "www.thefamouspeople.com/profiles/thumbs/mahatma-gandhi-36.jpg",
                "link": "www.thefamouspeople.com/profiles/mahatma-gandhi-55.php",
                "info": "['Listed In: Historical Personalities', ]",
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