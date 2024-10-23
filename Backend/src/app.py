from fastapi import FastAPI
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

