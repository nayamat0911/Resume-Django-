
from .import views
from django.urls import path

urlpatterns = [
   
    path('', views.Program, name='services_page'),
   

]
