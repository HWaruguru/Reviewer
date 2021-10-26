from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Project, Rating, Profile
from .forms import ProjectForm, SignUpForm, UpdateUserForm, UpdateUserProfileForm




def index(request):
     projects = Project.objects.all()
     return render(request, 'index.html', {"projects":projects})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    projects = request.user.projects.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {"projects": projects, 'user_form': user_form, 'prof_form': prof_form})

@login_required(login_url='login')
def search_projects(request):
    if 'title' in request.GET and request.GET['title']:
        title = request.GET.get("title")
        projects = Project.objects.filter(title__icontains=title)
        if len(projects) > 0:
            return render(request, 'search_result.html', {"projects": projects})
    return redirect('index')
