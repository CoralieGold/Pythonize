from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your models here.

class Article(models.Model):
   titre = models.CharField(max_length=100)
   contenu = models.TextField(null=True)
   part = models.CharField(max_length=100)
   image = models.CharField(max_length=100)

class PythonizeUser(User):
	doneTutorials = ArrayField(ArrayField(models.IntegerField()), blank=True)