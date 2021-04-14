from django.urls import path
from . import views

urlpatterns = [
    path ('', views.star_home, name='star_home')
]