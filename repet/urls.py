from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^is_teacher$', views.is_teacher, name='is_teacher'),#TODO
]
