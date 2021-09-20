from django.urls import path
from .views import CategoryListApiView

urlpatterns = [
    path('', CategoryListApiView.as_view()),
]