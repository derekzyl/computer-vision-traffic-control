
import os
import random
import string
import threading
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

    print(f"data1: {data1} , data2: {data2} , data3: {data3} , data4: {data4}")

    x_green_time = calculate_light_time(max_in_x=max(data1['total_count'], data2['total_count']), max_in_y=max(data3['total_count'], data4['total_count']),  type="x")
    y_green_time = calculate_light_time(max_in_x=max(data1['total_count'], data2['total_count']), max_in_y=max(data3['total_count'], data4['total_count']),  type="y")
   
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
    data_to_save = {
            "id":m,
            'x1_vehicles':data1['total_count'],
            
            'x2_vehicles':data2['total_count'],
            

            'y1_vehicles':data3['total_count'],
                'y2_vehicles':data4['total_count'],
            
            'x_green_time':x_green_time,
            'y_green_time':y_green_time,
            
        
            
        }
    try:
            save = Traffic(**data_to_save)
            db.add(save)
            db.commit()
    except Exception as db_exception:
            print(f"An error occurred while saving to the database: {db_exception}")

    return data_to_save







# def save_file(file: UploadFile):
#     if not os.path.exists(UPLOAD_DIRECTORY):
#         os.makedirs(UPLOAD_DIRECTORY)

#     file_path = os.path.join(UPLOAD_DIRECTORY, file.filename) # type: ignore
#     with open(file_path, "wb") as buffer:
#         buffer.write(file.file.read())

#     return file.filename

# async def processImage(x_1: UploadFile, x_2: UploadFile, y_1: UploadFile, y_2: UploadFile, db: Session):
#     try:
#         xx1 = save_file(x_1)
#         xx2 = save_file(y_1)
#         yy1 = save_file(x_2)
#         yy2 = save_file(y_2)

#         dir1 = f'uploads/{xx1}'
#         dir2 = f'uploads/{xx2}'
#         dir3 = f'uploads/{yy1}'
#         dir4 = f'uploads/{yy2}'

#         # Dictionary to hold the results of the callLight function
#         results = {}

#         # Define a function to call the 'callLight' function
#         def call_light_threaded(source, variable_name):
#             results[variable_name] = callLight(source=source)

#         # Create threads for each callLight function
#         threads = []
#         for source, variable in zip([dir1, dir2, dir3, dir4], ['data1', 'data2', 'data3', 'data4']):
#             thread = threading.Thread(target=call_light_threaded, args=(source, variable))
#             threads.append(thread)
#             thread.start()

#         # Wait for all threads to complete
#         for thread in threads:
#             thread.join()

#         # Print the results (optional)
#         for variable, data in results.items():
#             print(f"{variable}: {data}")

#         # Calculate x_green_time and y_green_time after all threads have completed
#         x_green_time = calculate_light_time(max_in_x=max(results['data1']['total_count'], results['data2']['total_count']),
#                                             max_in_y=max(results['data3']['total_count'], results['data4']['total_count']),
#                                             type="x")
#         y_green_time = calculate_light_time(max_in_x=max(results['data1']['total_count'], results['data2']['total_count']),
#                                             max_in_y=max(results['data3']['total_count'], results['data4']['total_count']),
#                                             type="y")

#         N = 10
#         me: uuid.UUID = uuid.uuid4()
#         j: str = str(me)
#         k: list[str] = j.split("-")
#         res: str = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))

#         l: str = "".join(k)
#         g = datetime.utcnow()
#         hh = g.strftime("%Y%m%d%H%M%S")
#         m: str = hh + res + l

#         data_to_save = {
#             "id": m,
#             'x1_vehicles': results['data1']['total_count'],
#             'x2_vehicles': results['data2']['total_count'],
#             'y1_vehicles': results['data3']['total_count'],
#             'y2_vehicles': results['data4']['total_count'],
#             'x_green_time': x_green_time,
#             'y_green_time': y_green_time
#         }

#         try:
#             save = Traffic(**data_to_save)
#             db.add(save)
#             db.commit()
#         except Exception as db_exception:
#             print(f"An error occurred while saving to the database: {db_exception}")

#         return data_to_save
#     except Exception as e:
#         print(f"An error occurred: {e}")
       
