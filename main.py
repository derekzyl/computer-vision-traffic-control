



from functools import lru_cache

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from module.traffic.controller import ProcessRoute

app:FastAPI = FastAPI()

app.include_router(ProcessRoute)

@app.get("/")
async def info() -> JSONResponse:
    return JSONResponse(status_code= status.HTTP_200_OK, content={"message":"welcome to smart traffic light "})
    









