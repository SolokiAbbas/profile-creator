from django.shortcuts import render
from accounts.forms import UserForm, ProfileForm, UserProfileForm
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.db import transaction

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
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
            profile = user.userprofile
            profile.bio = request.POST['bio']
            profile.save()
            user.save()
            registered = True
            login(request, user)
        else:
            print(user_form.errors)
    else:
        user_form = UserForm
    return render(request, 'accounts/register.html',
                        {'user_form':user_form, 'registered': registered,})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        passwordchange = False
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            if request.POST['password']:
                passwordchange = True
                user_form = user_form.save()
                user_form.set_password(request.POST['password'])
            user_form.save()
            profile_form.save()
            if passwordchange:
                login(request, user_form)
            return render(request, 'index.html')
        else:
            print('Please correct the error below.')
    else:
        user_form = UserProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/profile_detail.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


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
    model = UserProfile
    template_name = 'accounts/profile_detail.html'
