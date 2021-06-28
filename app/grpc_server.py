from concurrent import futures
import grpc

from app.generated import meter_usage_pb2_grpc
from app.meter_usage.grpc_service import MeterUsageService
from app.meter_usage.config import GRPC_PORT


class GRPCServer:
    """
    GRPC Server class
    """
    @staticmethod
    def run():
        """
        Staring the GRPC Server
        """
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=6))
        meter_usage_pb2_grpc.add_MeterUsageServiceServicer_to_server(
            MeterUsageService(), server
        )
        server.add_insecure_port(f"[::]:{GRPC_PORT}")
        server.start()
        server.wait_for_termination()


if __name__ == "__main__":
    """
    Start the GRPC Server
    """
    GRPCServer.run()
