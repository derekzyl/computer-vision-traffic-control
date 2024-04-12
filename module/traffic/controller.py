import json
import random
import string
import uuid
from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, File, Request, UploadFile, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import Json
from sqlalchemy.orm import Session
from starlette.datastructures import UploadFile

from config.database.index import get_db
from module.traffic.model import Traffic
from module.traffic.service import processImage

ProcessRoute = APIRouter(prefix="/process")



@ProcessRoute.post("/")
async def process(file: Request, db=Depends(get_db)):


    data =await  file.form()   
    print(data)

    

    if isinstance(data['x1'], UploadFile) and isinstance(data['x2'], UploadFile) and isinstance(data['y1'], UploadFile) and isinstance(data['y2'], UploadFile):

        x1:UploadFile = data.get('x1') # type: ignore
        x2: UploadFile = data.get('x2')# type: ignore
        y1: UploadFile  = data.get('y1')# type: ignore
        
        y2: UploadFile  = data.get('y2')# type: ignore
     
        return await processImage(x1, x2, y1, y2, db) # type: ignore
    
    # Return default values if files are not present or not of the expected type
    else:
        return  {
        
        'x1_vehicles': 20,
        'x2_vehicles': 12,
        'y1_vehicles': 45,
        'y2_vehicles': 23,
        'x_green_time': 60,
        'y_green_time': 60,
    }

@ProcessRoute.get("/")
async def get_process(db= Depends(get_db)):

    query = db.query(Traffic).all()
    dd = jsonable_encoder(query)
    

    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={
            "message": "successfully fetched",
            "gotten_data":dd,
            "status": True,
        },
    )
    
    
    #     return 60, 60
@ProcessRoute.post("/test")
async def post_process(db: Session = Depends(get_db)):

    N = 10
    me: uuid.UUID = uuid.uuid4()
    j: str = str(me)
    k: list[str] = j.split("-")
    res: str = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))

    l: str = "".join(k)
    g = datetime.utcnow()
    hh = g.strftime("%Y%m%d%H%M%S")
    m: str = hh + res + l

    data = {
        "id": m,
        'x1_vehicles': 23,
        'x2_vehicles': 12,
        'y1_vehicles': 45,
        'y2_vehicles': 23,
        'x_green_time': 33,
        'y_green_time': 23,
    }

    save = Traffic(**data)
    db.add(save)
    db.commit()
    
    # Convert Traffic object to a dictionary
    saved_data = jsonable_encoder(save)

    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={
            "message": "successfully created",
            "gotten_data": saved_data,
            "status": True,
        },
    )    
    




    





