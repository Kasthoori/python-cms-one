from django.urls import path
from .views import RoomView

urlpatterns = [
    path('hello', RoomView.as_view())
]
