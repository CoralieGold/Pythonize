from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
import json

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Article(models.Model):
   titre = models.CharField(max_length=100)
   contenu = models.TextField(null=True)
   part = models.CharField(max_length=100)
   image = models.CharField(max_length=100)



class ListField(models.TextField):
    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return value

    def get_prep_value(self, value):
        if value is None:
            return value

        return str(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mail = forms.EmailField(help_text='Required. A valid email address, please.')
    newsletter = forms.BooleanField(help_text='If checked, you accept to receive newsletters when new article is online.', required=True)
    tutosDone = ListField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

