from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Required. A valid email address, please.', max_length=500)
    newsletter = forms.BooleanField(help_text='If checked, you accept to receive newsletters when new article is online.', required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'newsletter')