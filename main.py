from fastapi import FastAPI,Request
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
@app.post("/uploads/")
async def upload_image(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))
    
    # Save the image to a temporary file
    temp_file_path = 'temp_img.jpg'
    image.save(temp_file_path)
    
    # Call the predict function using subprocess.Popen
    results=subprocess.Popen(["python", "predictWithOCR.py", "model='best.pt'", f"source={temp_file_path}"], stdout=subprocess.PIPE)
    output, error = results.communicate()
    
    # Delete the temporary file
    os.remove(temp_file_path)
    i= get_image_data_from_blob()
    
   # file_path = "runs/detect/train/temp_img.jpg"  # replace with your actual file path
    # Return the output
    return Response(content=i, media_type='image/jpeg')
    
    
   
    
