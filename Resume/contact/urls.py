
from .import views
from django.urls import path

urlpatterns = [
   
    path('', views.Contact, name="contact_page"),
   

]
