import http

from django.contrib.auth.decorators import login_required

from .forms import LoginUser,CustomUserCreationForm, UploadedFileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from .models import UploadedFile




# Create your views here.

def index(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            return HttpResponseRedirect('/login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'index.html',context)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile')
    if request.method == "POST":
        form = LoginUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile')
            else:
                return render(request, 'pages/login.html', {'form': form})
    else:
        form = LoginUser()
    context = {
        'form':form
    }

    return render(request,'pages/login.html', context)


@login_required
def profile(request):

    objects_list = UploadedFile.objects.filter(user_id=request.user.id)
    if request.method == "POST":
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            name = form.cleaned_data['name']

            user = User.objects.get(pk=request.user.pk)

            storage = UploadedFile.objects.create(
                name=name,
                file=file,
                user_id=user
            )
            storage.save()

            return HttpResponseRedirect('/profile')
    else:
        form = UploadedFileForm()

    context = {
        'user': request.user,
        'form': form,
        'auth': True,
        'objects_list': objects_list,
    }
    return render(request, 'pages/profile.html', context)
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')



