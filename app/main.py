import uvicorn
from fastapi import FastAPI

from app.core import config

app = FastAPI(
    docs_url=f"{config.API_PREFIX}/docs",
    redoc_url=f"{config.API_PREFIX}/redocs",
    title="Work Guard Application Layer",
    description="Fast API application for work guard coaching application",
    version="0.0.1",
    openapi_url=f"{config.API_PREFIX}/openapi.json",
)





if __name__ == "__main__":
    uvicorn.run(
        app, host="0.0.0.0", port=8081, proxy_headers=True, forwarded_allow_ips="*"
    )