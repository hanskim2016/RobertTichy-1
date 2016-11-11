from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^random_word/push', views.randomWordButton),
	url(r'^random_word', views.randomWord),
	url(r'^$', views.index)
]
    # url(r'^users', views.show_users)
    # url(r'^admin/', admin.site.urls),
