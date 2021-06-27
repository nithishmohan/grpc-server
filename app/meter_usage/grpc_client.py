from __future__ import print_function

import logging
import grpc

from datetime import datetime

from google.protobuf.json_format import MessageToDict

from app.generated import meter_usage_pb2
from app.generated import meter_usage_pb2_grpc

from app.meter_usage.config import GRPC_HOST, GRPC_PORT


class GRPCClient:

    @staticmethod
    def run(page=1, page_size=20):
        resp = []
        with grpc.insecure_channel(f"{GRPC_HOST}:{GRPC_PORT}") as grpc_channel:
            stub = meter_usage_pb2_grpc.MeterUsageServiceStub(grpc_channel)
            resp = stub.GetMeterUsage(
                meter_usage_pb2.MeterUsageRequest(page=page, page_size=page_size)
            )

        return MessageToDict(resp)


# if __name__ == "__main__":
#     logging.basicConfig()
#     results = run()
#     for result in results:
#         print(result)
