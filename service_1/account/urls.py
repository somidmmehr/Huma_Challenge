from django.urls import path
from .views import UserViewSet, LoginView

urlpatterns = [
    path('', UserViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('login/', LoginView.as_view())
]