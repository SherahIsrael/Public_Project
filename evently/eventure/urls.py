from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('users/', views.users, name='users'),
    path('users/details/<int:id>', views.details, name='details')
]