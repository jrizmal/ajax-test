from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^zapisek/izbris/', views.izbrisiZapisek, name='brisanje'),
    url(r'^iskanje/', views.vrniZadetke, name='zadetki'),
    url(r'^zapisek/', views.vrniZapisekGet, name='iskanje'),
    url(r'^ustvari/', views.ustvariZapisek, name='ustvari'),
    url(r'^zapiski/(\d+)/$', views.dobiZapisek, name='dobi_zapisek'),
    url(r'^zapiski/', views.vsiZapiski, name='vsi_zapiski'),
    
]
