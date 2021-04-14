from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_home, name='event_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('rating', views.rating, name='rating')
]
