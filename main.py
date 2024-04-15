



from functools import lru_cache

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from module.traffic.controller import ProcessRoute

app:FastAPI = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify specific origins instead of "*"
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
app.include_router(ProcessRoute)

@app.get("/")
async def info() -> JSONResponse:
    return JSONResponse(status_code= status.HTTP_200_OK, content={"message":"welcome to smart traffic light "})
    








