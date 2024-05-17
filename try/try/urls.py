"""
URL configuration for try project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls), 

    path('project/',projectt,name='project'),
    path('about/',aboutt,name='about'),
    path('booking/',bookingg,name='booking'),
    path('menu/',menuu,name='menu'),
    path('chef/',cheff,name='chef'),
    path('contact/',contactt,name='contact'),
    path('feature/',featuree,name='feature'),
    path('login/',login_page,name="login_page"),
    path('logout/',logout_page,name='logout_page'),
    path('register/',register,name="register"),
    path('show/',showw,name="show"),
    path('cart/',cartt,name="cart"),
    path('order/',orderr,name='order'),
    path('myorder/',myorders,name='myorders'),
    path('profile/',profilee,name='profile')
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns() 

