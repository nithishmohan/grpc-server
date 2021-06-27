import logging
import uvicorn

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.meter_usage.grpc_client import GRPCClient
from http import HTTPStatus

app = FastAPI()

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
templates = Jinja2Templates(directory="site")
app.mount("/static", StaticFiles(directory="site"), name="static")

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


@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
