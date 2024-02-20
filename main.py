from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.
templates=Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})
