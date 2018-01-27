from django.shortcuts import render
from accounts.forms import UserForm
from . import models
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, DetailView

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def digital(request):
    return render(request, 'digital.html')

def analog(request):
    return render(request, 'analog.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            login(request, user)
        else:
            print(user_form.errors)
    else:
        user_form = UserForm
    return render(request, 'accounts/register.html',
                        {'user_form':user_form, 'registered': registered})

@login_required
def current_user(request):
    current = request.user
    # profile = User.objects.get(username=current.username)
    bio = models.UserProfile.objects.all().filter(user=current)
    print(models.UserProfile.objects.all().filter(user=current))
    return render(request,'accounts/profile_detail.html',{"username":current.username,
                                                            "email":current.email,})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'accounts/user_login.html', {"errors":"Invalid", "username":username})
    else:
        return render(request, 'accounts/user_login.html', {})

class ProfileDetail(DetailView):
    context_object_name = 'profile_detail'
    model = models.UserProfile
    template_name = 'accounts/profile_detail.html'
