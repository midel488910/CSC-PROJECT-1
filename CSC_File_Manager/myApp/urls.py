
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Base, name ="Base"),
    path('Home/', views.Home, name ="Home"),
    path('Home/details/<int:id>', views.Details, name ="Details"),
    path('Home/create/', views.Create, name ="Create"),
]
