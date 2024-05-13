from django.urls import path, include
from . import views

#URLs to register their respective pages
urlpatterns = [
    path('', views.PDFView, name ="Home"),
    path('Home/', views.PDFView, name="Home"),
    path('home/', views.PDFView, name="Home"),
    path('Register/',views.SignUp, name="Signup"),
    path('register/',views.SignUp, name="Signup"),
    path('logout/',views.logout_view, name="logout"),
    path('create-post/',views.upload_pdf, name="create"),
    path('search/', views.search_view, name='search_view'),

    

]

