from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$'), views.index),
    url(r'^earn/', views.earn),
    url(r'^gamble/', views.gamble)
]