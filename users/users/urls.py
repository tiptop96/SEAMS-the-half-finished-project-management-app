"""users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import login
from login import views as lviews
from seams import views as sviews

urlpatterns = [
    url(r'^$', lviews.start_page),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login),
    url(r'^', include('seams.urls'), name='seams'),
    #url(r'^projects/', sviews.projects_page),
    url(r'^logout/$', lviews.logout_page),
    url(r'^update/$', lviews.update_profile),
    #url(r'^user/(\w+)/$', user_page),
]
