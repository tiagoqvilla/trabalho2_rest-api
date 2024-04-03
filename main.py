from fastapi import FastAPI, HTTPException
import json
from typing import Optional, Union
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

@app.put("/states/{id}", response_model=Registro)
async def update(id: int, request: Registro):
    for state_data in data:
        if state_data["no"] == id:
            state_data["state"] = request.state
            state_data["cases_under_investigation"] = request.cases_under_investigation
            state_data["cases_confirmed"] = request.cases_confirmed
            state_data["cases_discarded"] = request.cases_discarded
            state_data["cases_reported_total"] = request.cases_reported_total
            with open("dataset.json", "w") as file:
                json.dump(data, file, indent=4, default=str)
            return state_data
    raise HTTPException(status_code=404, detail="State not found")


@app.delete("/states/{id}")
async def delete(id: int):
    for state_data in data:
        if state_data["no"] == id:
            data.remove(state_data)
            with open("dataset.json", "w") as file:
                json.dump(data, file, indent=4, default=str)
            return "Deleted"
    raise HTTPException(status_code=404, detail="State not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)