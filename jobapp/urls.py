from django.urls import path, re_path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.details, name='details'),
    re_path(r'^[\w]+/actionUrl', views.yourSend, name='sendemail'),
]