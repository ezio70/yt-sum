from src.main import main
import fastapi
from fastapi import FastAPI
from fastapi import HTTPException
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/summary")
def get_summary(url: str):
    try:
        return main(url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))