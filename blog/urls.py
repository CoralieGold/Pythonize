from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^tutorials/$', views.tutorials),
    url(r'^tutorials/part/(\d+)$', views.tuto),
    url(r'^about$', views.about),
    url(r'^signUp$', views.sign_up),
    url(r'^login$', views.log_in),
    url(r'^logout$', views.log_out),
]
