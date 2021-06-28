from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

VERSION = "1.0.0"

config = Config(".env")

RDS_HOST: str = config("RDS_HOST", cast=str, default="mysql_app")
RDS_PORT: int = config("RDS_PORT", cast=int, default=3306)
RDS_PASSWORD: str = config("RDS_PASSWORD", cast=str, default='password')
RDS_USER: str = config("RDS_USER", cast=str, default='user')
RDS_DB: str = config("RDS_DB", cast=str, default='meter_db')
RDS_DBTYPE: str = config("RDS_DBTYPE", cast=str, default='mysql')

GRPC_HOST: str = config("GRPC_HOST", cast=str, default="grpc_server")
GRPC_PORT: int = config("GRPC_PORT", cast=int, default=50051)

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)
