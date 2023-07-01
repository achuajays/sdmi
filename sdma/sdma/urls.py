"""sdma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('al',views.alert,name="alert"),
    path('',views.logr,name="logr"),
    path('reg/<int:id>',views.update,name="update"),
    path('em',views.em,name="em"),
    path('team',views.team,name="team"),
    path('teamlogin',views.logteamr,name="logteamr"),
    path('alertr',views.alertr,name="alertr"),
    path('reffunn',views.reffunn,name="reffunn"),
    path('updatereffun/<int:id>',views.updatereffun,name="updatereffun"),
    path('food',views.foodr,name="foodr"),
    path('foodu',views.foodu,name="foodu"),
    path("news_catcher/", views.news_catcher, name="news_catcher"),
    path("waste", views.wastee, name="wastee"),
    path("updatewaste", views.wasteview, name="wasteview"),
    path("index", views.index, name="index"),
    path('news', views.indexx, name ='indexx'),
    path('esr', views.esr, name ='esr'),


]

