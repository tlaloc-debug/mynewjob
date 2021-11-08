from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.details, name='details'),
    path(r'^(?P<slug>[\w-]+)/actionUrl', views.yourSend),
]