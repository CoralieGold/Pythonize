#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from blog import models, forms

def home(request):
	return render(request, 'blog/index.html', {'nav': 'home'})

def sign_up(request):
	if(request.user.is_authenticated()):
		return redirect(home)
	if request.method == 'POST':
		form = forms.SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			user.profile.email = request.POST.get('email', '')
			user.profile.newsletter = request.POST.get('newsletter', '')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect(home)
	else:
		form = forms.SignUpForm()
	return render(request, 'registration/sign_up.html', {'form': form})

def about(request):
	return render(request, 'blog/about.html', {'nav': 'about'})

def tutorials(request):
	articles = models.Article.objects.all()

	if(request.user.is_authenticated()):
		userConnected = True
		doneArticles = request.user.profile.tutosDone
	else:
		userConnected = False
		doneArticles = []

	return render(request, 'blog/tutorials.html', {'nav': 'tuto', 'articles': articles, 'userConnected': userConnected, 'doneArticles': doneArticles})

def tutorials_details(request, part):
	if int(part) > 10:
		return redirect(home)
	article = models.Article.objects.get(part=part)

	if(request.user.is_authenticated()):
		if request.method == 'POST' and part not in request.user.profile.tutosDone:
			user = request.user
			tutosDone = list(user.profile.tutosDone)
			tutosDone.append(str(part))
			user.profile.tutosDone = tutosDone
			user.save()     
			
		userConnected = True
		articleDone = True if part in request.user.profile.tutosDone else False
	else:
		userConnected = False
		articleDone = False

	return render(request, 'blog/tutorials_details.html', {'nav': 'tuto', 'article': article, 'userConnected': userConnected, 'done': articleDone })
