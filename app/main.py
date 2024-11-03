import uvicorn
from fastapi import FastAPI, Request, status
from starlette.responses import JSONResponse

from app.core import config
from app.api.routes import auth
from app.exceptions.exception_handler import TransactionException

app = FastAPI(
    docs_url=f"{config.API_PREFIX}/docs",
    redoc_url=f"{config.API_PREFIX}/redocs",
    title="Work Guard Application Layer",
    description="Fast API application for work guard coaching application",
    version="0.0.1",
    openapi_url=f"{config.API_PREFIX}/openapi.json",
)

app.include_router(auth.router)


@app.exception_handler(TransactionException)
async def transaction_exception_handler(request: Request, exc: TransactionException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": f"🚨Error occurred!  {exc.name}."},
    )


if __name__ == "__main__":
    uvicorn.run(
        app, host="0.0.0.0", port=8081, proxy_headers=True, forwarded_allow_ips="*"
    )
