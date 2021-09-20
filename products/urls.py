from django.urls import path
from .views import ProductsListApiView

urlpatterns = [
    path('', ProductsListApiView.as_view()),
]