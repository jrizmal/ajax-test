from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Zapisek(models.Model):
    naslov = models.CharField(max_length=50)
    besedilo = models.CharField(max_length=1000)
    ustvarjeno = models.DateTimeField(auto_now_add=True, auto_now=False)
    spremenjeno = models.DateTimeField(auto_now_add=False, auto_now=True)
    
