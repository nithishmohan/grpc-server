from concurrent import futures
import grpc

from app.generated import meter_usage_pb2_grpc
from app.meter_usage.grpc_service import MeterUsageService
from app.meter_usage.config import GRPC_PORT


class GRPCServer:
    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        meter_usage_pb2_grpc.add_MeterUsageServiceServicer_to_server(
            MeterUsageService(), server
        )
        server.add_insecure_port(f"[::]:{GRPC_PORT}")
        server.start()
        server.wait_for_termination()

"""
Start the GRPC Server
"""
if __name__ == "__main__":
    GRPCServer.run()
