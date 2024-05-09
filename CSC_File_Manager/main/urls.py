from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PDFView, name ="Home"),
    path('Home/', views.PDFView, name="Home"),
    path('home/', views.PDFView, name="Home"),
    path('Register/',views.SignUp, name="Signup"),
    path('register/',views.SignUp, name="Signup"),
    path('logout/',views.logout_view, name="logout"),
    path('create-post/',views.upload_pdf, name="create"),
    #path('upload-post/',views.upload_pdf, name="upload"),
    #path('pdf/',views.PDFView, name="upload"),   
    

]

