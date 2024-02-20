from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.
templates=Jinja2Templates(directory="templates")

@app.get("/abc")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/")
def home():
    return "Hello"
   
    
