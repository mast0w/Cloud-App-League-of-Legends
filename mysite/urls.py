from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^user/$', views.user, name="user"),
    url(r'^dataAnalyst/$', views.dataAnalyst, name="dataAnalyst"),
    url(r'^admin/$', views.admin, name="admin")
]


urlpatterns+=staticfiles_urlpatterns()