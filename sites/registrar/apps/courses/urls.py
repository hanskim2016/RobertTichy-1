from django.conf.urls import url, include
from django.contrib import admin
from . import views
# import re

urlpatterns = [
    url(r'^$', views.index),
    url(r'create$',views.create),
    url(r'^(\d+)/edit$',views.update),
    url(r'^(\d+)/delete$',views.delete),
    url(r'^(\d+)$',views.showCourse),
]
