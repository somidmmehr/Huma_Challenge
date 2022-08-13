from django_grpc_framework.test import RPCTestCase
from protos import account_pb2, account_pb2_grpc
from .models import CustomUser


class PostServiceTest(RPCTestCase):
    def test_create_post(self):
        stub = account_pb2_grpc.UserControllerStub(self.channel)
        response = stub.Create(account_pb2.User(username='test_name', email='test_email@gango.grpc.com'))
        self.assertEqual(response.username, 'test_name')
        self.assertEqual(response.email, 'test_email@gango.grpc.com')
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_list_posts(self):
        CustomUser.objects.create(username='test_name_1', email='test_email_1@gango.grpc.com')
        CustomUser.objects.create(username='test_name_2', email='test_email_2@gango.grpc.com')
        stub = account_pb2_grpc.UserControllerStub(self.channel)
        user_list = list(stub.List(account_pb2.UserListRequest()))
        self.assertEqual(len(user_list), 2)