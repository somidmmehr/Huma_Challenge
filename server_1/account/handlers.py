from .services import CustomUserService
from protos import account_pb2_grpc


def grpc_handlers(server):
    account_pb2_grpc.add_UserControllerServicer_to_server(CustomUserService.as_servicer(), server)
