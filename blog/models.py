from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):

   titre = models.CharField(max_length=100)

   contenu = models.TextField(null=True)
   
   part = models.CharField(max_length=100)
   
   image = models.CharField(max_length=100)
