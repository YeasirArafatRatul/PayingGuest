from django.shortcuts import render
from django.views.generic import CreateView,ListView, DetailView
from django.http import HttpResponse
from .models import UserProfile
from forms.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post



# Create your views here..


def profile(request):
    return render(request, 'user_profile/UserProfile.html')
    