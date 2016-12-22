from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    
    url(r'^create/', views.ustvariZapisek, name='ustvari'),
    url(r'', views.vsiZapiski, name='ustvari'),
]
