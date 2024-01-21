from django.contrib import admin

from faq.models import Faq, AskInformation


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'useyn']
    list_filter = ['useyn']


@admin.register(AskInformation)
class AskAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'use_yn', 'get_status_display', 'email', 'reg_date']
    list_filter = ['use_yn']
