from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from accounts.models import Profile
import datetime
from django.utils.timezone import now

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def signup_view(request):

    form = SignUpForm(request.POST)
    model_profile = Profile(NumFollowers=0, LastUpdated=now)
    model_profile.save()
    # model_repo = Repository()
    # model_repo.save()
    if form.is_valid():
        form.save()
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    # NumFollowers=0
    return render(request, 'signup.html', {'form': form})

def set_attributes(name, followers=0, time=None):
    print(name)
    user, _ = Profile.objects.get_or_create(user=name)
    print(user.NumFollowers)
    user.NumFollowers = followers
    user.LastUpdated = time or datetime(2000, 1, 1, 1, 1, 1, 1)
    user.save()

