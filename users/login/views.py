from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def start_page(request):
    return render(request, 'main.html')

