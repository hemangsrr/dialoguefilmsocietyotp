"""dialoguewebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from base.views import HomeView
from preevents.views import EventsListView
from regionalscreening.views import ScreeningsView
from diff6.views import SampleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name='home'),
    path('preevent/', EventsListView, name='preevent'),
    path('regionalscreening/', ScreeningsView, name='regionalscreening'),
    path('diff6/', SampleView, name='diff6'),
]
