from fastapi import FastAPI, HTTPException
import json
from typing import List, Dict, Optional, Union
from pydantic import BaseModel

class Registro(BaseModel):
    state: str
    cases_under_investigation: Union[int, str]
    cases_confirmed: Union[int, str]
    cases_discarded: Union[int, str]
    cases_reported_total: Union[int, str]

app = FastAPI()

with open("dataset.json", "r") as file:
    data = json.load(file)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/states/")
async def read_states():
    return data


@app.get("/states/{state}")
async def read_state(state: str):
    for state_data in data:
        if state_data["state"].lower() == state.lower():
            return state_data
    raise HTTPException(status_code=404, detail="State not found")


@app.post("/states/")
async def create_state(state_data: Registro):
    new_state_data = state_data.dict()  
    new_state_data["no"] = len(data) + 1

    data.append(new_state_data)
    with open("dataset.json", "w") as file:
        json.dump(data, file, indent=4, default=str)
    return new_state_data
