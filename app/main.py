import logging
import uvicorn

from fastapi import FastAPI, HTTPException
from app.meter_usage.grpc_client import GRPCClient
from http import HTTPStatus


app = FastAPI()

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

logger = logging.getLogger("uvicorn.error")


@app.get("/")
async def root():
    return {"message": "Hello Nithish"}


@app.get(
    "/meterusages",
    name="meterusages:get-meterusages",
    response_model_exclude_unset=True
)
async def meter_usage(page: int = 1, page_size: int = 25):
    """

    :type page: int
    :type page_size: int
    """
    try:
        response = GRPCClient().run(page=page, page_size=page_size)
    except Exception as e:
        logging.critical(e, exc_info=True)
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Internal Server Error")

    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
