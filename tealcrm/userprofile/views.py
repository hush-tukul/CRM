from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from .models import Userprofile


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)

            return redirect('/log-in/')

    else:
        form = UserCreationForm()
    return render(request, 'userprofile/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                # Redirect to a success page or any other desired page
                return redirect('index')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = AuthenticationForm()

    return render(request, 'userprofile/login.html', {'form': form})
