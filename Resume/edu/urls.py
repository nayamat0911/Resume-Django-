
from .import views
from django.urls import path

urlpatterns = [
   
    path('', views.Edu, name='edu_page'),
   

]
