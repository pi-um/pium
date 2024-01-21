from django.contrib import admin
from reservation.models import ReservationConstraint, Reservation
# Register your models here.

@admin.register(Reservation)
class ManageReservation(admin.ModelAdmin):
    search_fields = ['user', 'userName', 'userEmail']
    list_display = ['user', 'status', 'course', 'reservation_many','reservation_date', 'reservation_hour', 'reservation_min']
    list_filter = ['status', 'course']

@admin.register(ReservationConstraint)
class ManageConstraint(admin.ModelAdmin):
    list_display = ['type', 'start_date', 'end_date', 'start_time','end_time']
