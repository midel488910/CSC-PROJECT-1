from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name ="Home"),
    path('Home/', views.Home, name="Home"),
    path('home/', views.Home, name="Home"),
    path('Register/',views.SignUp, name="Signup"),
    path('register/',views.SignUp, name="Signup"),
    path('logout/',views.logout_view, name="logout"),
    path('create-post',views.create_post, name="create"),
    path('upload-form',views.upload_form, name="upload-form"),

]

