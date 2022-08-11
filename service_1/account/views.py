from rest_framework import viewsets, status
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response("list OK", status=status.HTTP_200_OK)

    def create(self, request):
        return Response("create OK", status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        return Response(f"retrieve {pk} OK", status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        return Response(f"update {pk} OK", status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        return Response(f"destroy {pk} OK", status=status.HTTP_200_OK)
