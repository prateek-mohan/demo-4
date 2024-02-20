from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})
