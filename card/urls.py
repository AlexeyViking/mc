from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.card_base, name='card_base'),
    url(r'^mail.*$', views.mail, name='mail'),
]
