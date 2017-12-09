#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
import models

def home(request):
    return render(request, 'blog/index.html', {'nav': 'home'})
    
def sign_in(request):
    return render(request, 'blog/sign_in.html', {'nav': 'home'})
    
def sign_up(request):
    return render(request, 'blog/sign_up.html', {'nav': 'home'})
   
def about(request):
    return render(request, 'blog/about.html', {'nav': 'about'})

def tutorials(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/tutorials.html', {'nav': 'tuto', 'articles': articles})
    
def tutorials_details(request, part):
	if int(part) > 10:
		return redirect(home)
	article = models.Article.objects.get(part=part)
	print(article)
	return render(request, 'blog/tutorials_details.html', {'nav': 'tuto', 'article': article})
