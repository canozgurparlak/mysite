from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^download/', views.download, name='download'),
    url(r'^einleitung/', views.einleitung, name='einleitung'),
    ]