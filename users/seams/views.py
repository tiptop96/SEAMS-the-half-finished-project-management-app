from django.shortcuts import render
from django.views.generic.edit import UpdateView
from seams.models import Project, Event
from seams.forms import ProjectForm, EventForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
import seams

# Create your views here.
def projects_page(request):
    return render(request, 'user.html', { 'user': request.user })

def cal_page(request):
    pass

#Change to: "Process more than on form at once"
#https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
def add_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            pro = project_form.save()
            pro.authors.add(request.user) #add user to the project
            pro.save()

            return redirect('/projects/')
        else:
            pass
    else:
        project_form = ProjectForm()
    return render(request, 'add.html', {'project_form': project_form, })



def update_project(request, pk):
    projectInst = Project.objects.get(pk=pk)
    events = Event.objects.filter(project = projectInst).filter(eventtype='E').order_by('datetime')
    tasks = Event.objects.filter(project = projectInst).filter(eventtype='T').order_by('datetime')
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            proEvent = event_form.save(commit=False)
            proEvent.project = projectInst #Forcibly set the project inst to the on on the page.
            proEvent.save()
            return redirect(projectInst)
        else:
            pass
    return render(request, 'seams/project_form.html', {
        'event_form': EventForm(),
        'project': projectInst,
        'events': events,
        'tasks': tasks,
    })

def delete_event(request, pk):
    event = Event.objects.get(pk=pk)
    projectInst=event.project
    if request.user.is_staff:
        event.delete()
        messages.success(request, "Your comment was successfully deleted.")
        return redirect(projectInst)
