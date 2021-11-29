from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse

from app.server.database.dict import TransEG, TransMR

from app.server.models.dict import (
    ErrorResponseModel,
    ResponseModel,
)

router3 = APIRouter()

# TEG = TransEG("india")
# TEG.TransEG_mean()
# TEG.TransEG_syn()
# TEG.TransEG_exmple()

@router3.get("/")
async def get_dict():
    html_content = """
    <html>
        <head>
            <title>Dictionary Home</title>
        </head>
        <body>
            English dictionary Translation: <a class="nav-link" href="/dict/translate/" target="_blank"> /translate/{word}</a>
            <br>
            English to marathi dictionary Translation: <a class="nav-link" href="/dict/translateTo/marathi/" target="_blank"> /translateTo/marathi/{word}</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@router3.get("/translate/{word}", response_description="Data retrieved")
async def get_dict(word: str):
    # word = "india"
    TEG = TransEG(word)
    mean = TEG.TransEG_mean()
    syn = TEG.TransEG_syn()
    exmp = TEG.TransEG_exmple()
    if mean==None or syn==None or exmp==None:
        print("Some Exception Ocure translate....")
        return ErrorResponseModel("An error occurred.", 404, "Data doesn't exist.")
    data = {"Word":word, "Meanings":mean, "Synonyms":syn, "Example Sentences": exmp}
    return ResponseModel(data, "Data retrieved successfully")

@router3.get("/translateTo/marathi/{word}", response_description="Data retrieved")
async def get_dict2(word: str):
    # word = "india"
    TEG = TransMR(word)
    mean, example = TEG.TransToMR()
    if mean ==None or example==None:
        print("Some Exception Ocure in translateTo/marathi....")
        return ErrorResponseModel("An error occurred.", 404, "Data doesn't exist.")
    data = {"Word":word, "Meanings":mean, "Example Sentences": example}
    return ResponseModel(data, "Data retrieved successfully")
