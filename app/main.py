from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
import uvicorn

from api.v1.routes.ergopay import ergopay_router

app = FastAPI(
    title='ergopad-ergopay',
    docs_url="/api/docs",
    openapi_url="/api"
)

#region Routers
app.include_router(ergopay_router, prefix="/api/ergopay", tags=["ergopay"])
#endregion Routers

origins = [
    "https://*.ergopad.io"
]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/ping")
async def ping():
    return {"hello": "world"}

# MAIN
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=7000)
