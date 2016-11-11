from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^jas/([a-zA-Z]+)$', views.index),
    url(r'^jas/', views.index),
]
