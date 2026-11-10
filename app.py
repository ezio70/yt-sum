from src.main import main
import fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/summary")
def get_summary(url: str):
    try:
        return main(url)
    except Exception as e:
        return {"error": str(e)}