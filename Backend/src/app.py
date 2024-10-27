from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os
import logging
import mqtt_func
from project_dirs import FRONTEND_DIR
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

mqtt_func.connect()

app = FastAPI()

PICTURE_FILE_NAME = ""

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/photo/")
async def upload_image(request: Request):
    try:
        save_path = FRONTEND_DIR / 'public/received_images'

        logging.info("APP - Image Save Path: %s", save_path)
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'{timestamp}.jpg'
        file_path = os.path.join(save_path, filename)

        with open(file_path, "wb") as buffer:
            data = await request.body()
            buffer.write(data)

        return JSONResponse(content={"message": "Image successfully saved", "filename": filename}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": f"Error: {str(e)}"}, status_code=500)


@app.get("/getInfo")
async def getInfoFromESP():
    # return JSONRESPONSE
    if not mqtt_func.data_queue.empty():
        res = mqtt_func.data_queue.get()
        res["filename"] = "20241027_214422.jpg"
        return res

