"""frontend URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

import cats.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', cats.views.index),
    url(r'^cats$', cats.views.cats, name="cat_list"),
    url(r'^cats/(\w+)$', cats.views.single_cat, name="single_cat"),
    url(r'^breeds$', cats.views.breeds, name="breed_list"),
    url(r'^breeds/(\w+)$', cats.views.single_breed, name="single_breed"),
]
