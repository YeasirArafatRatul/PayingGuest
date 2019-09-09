from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model, logout
from django.utils.http import is_safe_url
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, FormView
from .models import User
from user_profile.models import UserProfile
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm

# Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'forms/registration.html'
    success_url = '/login/'


# Create your views here.
@login_required
def updateprofile(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        image_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
       
        if update_form.is_valid() and image_form.is_valid():
        	update_form.save()
        	image_form.save()
        	return redirect('profile')
       


    else:
        update_form = UserUpdateForm(instance=request.user)
        image_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'update_form': update_form,
        'image_form': image_form,
    }

    return render(request, 'user_profile/ProfileUpdate.html', context)






























# def registration(request, *args, **kwargs):
#     form = SignUpForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form': form
#     }
#     return render(request, "registration.html", context)


# @login_required
# def login(request):
#     next = request.GET.get('next')
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect('/')

#     context = {
#         'form': form
#     }
#     return render(request, "login.html", context)




