from urllib import request

from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.reservationMain, name="reservationMain"),
    path("dateSearch/", views.dateSearch, name="dateSearch"),
    path("enrollReservation/", views.enrollReservation, name="enrollReservation"),
]

