from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news$', views.news, name='news'),
    url(r'^exercise$', views.exercise, name='exercise'),
]
