from google.protobuf.timestamp_pb2 import Timestamp
from app.generated import meter_usage_pb2, meter_usage_pb2_grpc
from app.meter_usage.models import MeterUsage

from app.meter_usage.database import get_session as db_session


class MeterUsageService(meter_usage_pb2_grpc.MeterUsageServiceServicer):

    def GetMeterUsage(self, request, context):
        """
        :param request:
        :param context:
        :return:
        """
        ##getting the meter usages from the database
        meter_usages = db_session().query(MeterUsage).limit(request.page_size).offset(
            (request.page - 1) * request.page_size)

        _meter_usages = []
        timestamp = Timestamp()
        for meter_usage in meter_usages:
            timestamp.FromDatetime(meter_usage.time)
            _meter_usages.append(
                meter_usage_pb2.MeterUsage(
                    id=meter_usage.id,
                    value=meter_usage.value,
                    time=timestamp,
                )
            )
        ##serializing the meter usages to MeterUsageResponse format
        return meter_usage_pb2.MeterUsageResponse(data=_meter_usages)
