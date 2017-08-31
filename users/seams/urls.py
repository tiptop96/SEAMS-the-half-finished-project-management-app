from django.conf.urls import url
from seams.models import Project
from django.views.generic import ListView, DetailView
from seams.views import projects_page, update_project, add_project, delete_event

urlpatterns = [
    url(r'^del_event/(?P<pk>\d+)/$', delete_event, name='del_event'),
    url(r'^projects/$', projects_page, name='projects'),
    url(r'^projects/add/$', add_project, name='add'),
    url(r'^projectdetails/(?P<pk>\d+)/$', update_project, name='projectdetails'), #Obs name is project (no 's')
]
