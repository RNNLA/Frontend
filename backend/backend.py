import json

from typing import Any
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from datetime import date, datetime

app = FastAPI()
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

today = date.today().strftime("%Y-%m-%d")
FILE_NAME = "data/" + today + "_VerificationNewsData.json"



class JsonData(BaseModel):
    data: list[dict[str, Any]]


@app.put("/")
def update_json(json_data: JsonData) -> None:
    with open(FILE_NAME, "w") as f:
        f.write(json.dumps(json_data.data, indent=4))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
