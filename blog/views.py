#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
import models

def home(request):
    return render(request, 'blog/index.html', {'nav': 'home'})
    
'''def login(request):
	if(request.user.is_authenticated()):
		return redirect(home)
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			request.user = authenticate(username=username, password=raw_password)
			login(request)
			return redirect(home)
	else:
		form = UserCreationForm()
	return render(request, 'blog/sign_in.html', {'nav': 'home'})'''
    
def sign_up(request):
	if(request.user.is_authenticated()):
		return redirect(home)
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			request.user = authenticate(username=username, password=raw_password)
			login(request)
			return redirect(home)
	else:
		form = UserCreationForm()

	return render(request, 'blog/sign_up.html', {'nav': 'home', 'form': form})
   
'''def logout(request):
	logout(request)
	return redirect(home)'''
  
def about(request):
    return render(request, 'blog/about.html', {'nav': 'about'})

def tutorials(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/tutorials.html', {'nav': 'tuto', 'articles': articles})
    
def tutorials_details(request, part):
	if int(part) > 10:
		return redirect(home)
	article = models.Article.objects.get(part=part)
	return render(request, 'blog/tutorials_details.html', {'nav': 'tuto', 'article': article})
