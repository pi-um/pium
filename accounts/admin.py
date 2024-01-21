from django.contrib import admin
from .models import User, RecommendMarkup, ReservationUser


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(RecommendMarkup)
class RecommendMarkupAdmin(admin.ModelAdmin):
    list_display = ['type', 'content']
    list_filter = ['type']

@admin.register(ReservationUser)
class ReservationUserAdmin(admin.ModelAdmin):
    search_fields = ['user', 'userName', 'userEmail']
    list_display = ['name', 'email', 'phone']



