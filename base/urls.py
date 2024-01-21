from urllib import request

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('faq/', include("faq.urls")),
    path('reservation/', include("reservation.urls")),
    path('aboutus/',TemplateView.as_view(template_name="aboutUs.html"), name="aboutUs"),
    path('program/basic/',TemplateView.as_view(template_name="program/basicExamine.html"), name="basicExam"),
    path('program/body/',TemplateView.as_view(template_name="program/bodyExamine.html"), name="bodyExam"),
    path('program/simple/',TemplateView.as_view(template_name="program/simpleExamine.html"), name="simpleExam"),
    path('program/pro/',TemplateView.as_view(template_name="program/proExamine.html"), name="proExam"),
    path('selftest/', TemplateView.as_view(template_name="selftest/selftest.html"), name="selftest"),
    path('program/consult/',TemplateView.as_view(template_name="program/consultExamine.html"), name="consultExam"),
    path("", views.index, name="main")
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include("debug_toolbar.urls")),
    ]
    
