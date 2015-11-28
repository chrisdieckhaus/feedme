from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'results', views.result, name='result'),
    url(r'profile', views.profile, name='profile'),
]