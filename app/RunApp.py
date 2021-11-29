from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from app.server.routes.country import router1 as CountryRouter

from app.server.routes.people import router2 as PeopleRouter

from app.server.routes.dict import router3 as DictRouter

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root(request: Request, ):
    templates = Jinja2Templates(directory="app/templates")
    return templates.TemplateResponse("index.html", {"request": request,})
    # return {"message": "Welcome to The Famous Peoples Project app!"}


app.include_router(CountryRouter, tags=["Country"], prefix="/country")

app.include_router(PeopleRouter, tags=["People"], prefix="/people")

app.include_router(DictRouter, tags=["Dictionary"], prefix="/dict")

# uvicorn app.RunApp:app --reload

# from app.data import d1
@app.get("/home/")
def read_root():
    return {"Hello": "World", "data": "hello"}