from django.urls import path
from . import views
urlpatterns = [
    path ('', views.gipsy, name='home'),
    path ('lv', views.lv, name='delivery'),
]