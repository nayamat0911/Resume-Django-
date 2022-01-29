from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.base_home),
    path('', include('home.urls')),
    path('edu/', include('edu.urls')),
    path('program/', include('program.urls')),
    path('contact/', include('contact.urls')),

]
