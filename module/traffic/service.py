
import os
import random
import string
import uuid
from datetime import datetime
from typing import Any

from fastapi import UploadFile
from sqlalchemy.orm import Session

from deep_sort.deep.reid.torchreid import data
from module.traffic.model import Traffic
from tracker import callLight
from traffic_time import calculate_light_time

UPLOAD_DIRECTORY = "uploads"

def save_file(file: UploadFile):
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)

    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename) # type: ignore
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file.filename
async def processImage ( x_1:UploadFile, x_2:UploadFile, y_1:UploadFile, y_2:UploadFile, db:Session):
    xx1= save_file(x_1)
    xx2= save_file(y_1)
    yy1= save_file(x_2)
    yy2= save_file(y_2)

    dir1 = f'uploads/{xx1}'
    dir2 = f'uploads/{xx2}'
    dir3 = f'uploads/{yy1}'
    dir4 = f'uploads/{yy2}'

    data1 = callLight(source= dir1)   
    data2 = callLight(source= dir2)
    data3 = callLight(source= dir3)
    
    data4 = callLight(source= dir4)

    x_green_time = calculate_light_time(max_in_x=max(data1['total_count'], data2['total_count']), max_in_y=max(data3['total_count'], data4['total']),  type="x")
    y_green_time = calculate_light_time(max_in_x=max(data1['total_count'], data2['total_count']), max_in_y=max(data3['total_count'], data4['total']),  type="y")
   
    N = 10
    me: uuid.UUID = uuid.uuid4()
    j: str = str(me)
    k: list[str] = j.split("-")
    res: str = "".join(
                random.choices(string.ascii_lowercase + string.digits, k=N)
            )

    l: str = "".join(k)
    g = datetime.utcnow()
    hh = g.strftime("%Y%m%d%H%M%S")
    m: str = hh + res + l
    #    x1_vehicles:Mapped[int]
    #     x2_vehicles:Mapped[int]
    #     y1_vehicles:Mapped[int]
        
    #     y2_vehicles:Mapped[int]
    #     x_green_time:Mapped[int]
    #     y_green_time:Mapped[int]
    dadta = {
            "id":m,
            'x1_vehicles':data1['total_count'],
            
            'x2_vehicles':data2['total_count'],
            

            'y1_vehicles':data3['total_count'],
                'y2_vehicles':data4['total_count'],
            
            'x_green_time':x_green_time,
            'y_green_time':y_green_time,
            
        
            
        }
    save = Traffic(**dadta) 
    db.add(save)
    
    db.commit()


    return x_green_time, y_green_time





