from typing import Annotated

from fastapi import APIRouter, Depends, File, Request, UploadFile
from fastapi.responses import JSONResponse
from pydantic import Json

from config.database.index import get_db
from module.traffic.model import Traffic
from module.traffic.service import processImage

ProcessRoute = APIRouter(prefix="/process")



@ProcessRoute.post("/")
async def process(request:Request, db=Depends(get_db)):

    print(len(request['x1']))

    # if isinstance(x1, UploadFile) and isinstance(x2, UploadFile) and isinstance(y1, UploadFile) and isinstance(y2, UploadFile):
    #     print(x1.filename, x2.filename, y1.filename, y2.filename)
    #     return await processImage(x1, x2, y1, y2, db)
    
    # Return default values if files are not present or not of the expected type
    # else:
    #     return 60, 60
@ProcessRoute.get("/")
async def get_process(db= Depends(get_db)):

    query = db.query(Traffic).all()

    return JSONResponse(content=query)
    
    



