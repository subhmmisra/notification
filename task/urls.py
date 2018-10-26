"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from login.views import *
#from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/',UsernameValidator.as_view()),
    url(r'^email/',EmailValidator.as_view()),
    url(r'^$', register, name='register_'),
    url(r'^home/$', Home.as_view(), name='home'),
    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success, name='register_success'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_page, name='logout_page'),
    url(r'^notification/create/$', AddUserDevice.as_view(), name="notification_create"),
    url(r'^notification/send/$', SendNotification.as_view(), name="send_notification"),
    #############################
    url(r'^accounts/', include('allauth.urls')),
     #############################
    url(r'^firebase-messaging-sw.js',(TemplateView.as_view(
        template_name="firebase-messaging-sw.js",
        content_type='application/javascript',
    )), name='firebase-messaging-sw')
    
    
]
