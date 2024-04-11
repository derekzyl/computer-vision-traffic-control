from fastapi import APIRouter, Depends, Request, UploadFile
from fastapi.responses import JSONResponse
from pydantic import Json

from config.database.index import get_db
from module.traffic.model import Traffic
from module.traffic.service import processImage

ProcessRoute = APIRouter(prefix="/process")



@ProcessRoute.post("/")
async def process(data:Request, db= Depends(get_db) ):
    if isinstance(data['x1'], UploadFile) and isinstance(data['x2'], UploadFile) and isinstance(data['y1'], UploadFile) and isinstance(data['y2'], UploadFile):
      

        x1 = data['x1']
        x2 = data['x2']
        y1 = data['y1']
        
        y2 = data['y2']

        return await processImage(x1, x2, y1, y2, db)

    else:
        return 60, 60

        


@ProcessRoute.get("/")
async def get_process(db= Depends(get_db)):

    query = db.query(Traffic).all()

    return JSONResponse(content=query)
    
    

