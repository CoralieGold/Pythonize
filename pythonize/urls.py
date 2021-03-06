"""pythonize URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from blog import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
# import newsletter

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tutorials/$', views.tutorials, name='tutorials'),
    url(r'^tutorials/part/(\d+)$', views.tutorials_details, name='tutorials_details'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^signUp$', views.sign_up, name='sign_up'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^newsletter/', include('newsletter.urls'))
]
