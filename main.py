from datetime import datetime
from fastapi import FastAPI
from CO2Meter import *

sensor = CO2Meter("/dev/hidraw0")
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/read")
def read_item():
    data = sensor.get_data()
    data.update({'timestamp': datetime.utcnow()})
    return data
