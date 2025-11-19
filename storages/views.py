from urllib.request import HTTPRedirectHandler

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

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