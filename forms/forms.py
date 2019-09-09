from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
from user_profile.models import UserProfile

# User = get_user_model()


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password','active')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(widget=forms.PasswordInput)

    def form_valid(self,form):
        request=self.request
        next_=request.GET.get('next')
        next_post=request.POST.get('next')
        redirect_path=next_ or next_post or None
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user=authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['UserProfile.html']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("login")
        return super(LoginView, self).form_invalid(form)





class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1=forms.CharField(label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email', 'full_name','phone','Gender','Address')

    def clean_password2(self):
        # Check that the two password entries match
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user=super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active=True  # send confirmation email
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['full_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['image']
































# from django.db import models
# from django import forms
# from .models import MyUser
# from django.contrib.auth import authenticate,get_user_model


# User = get_user_model()


# class SignUpForm(forms.ModelForm):
#   password = forms.CharField(label = 'password', widget = forms.PasswordInput)
#   confirm_password = forms.CharField(label= 'confirm password', widget=forms.PasswordInput)

#   class Meta:
#       model = User
#       fields = ['username',
#               'email',
#               'first_name',
#               'last_name',

#       ]
#   def clean_password(self):
#       email = self.cleaned_data.get('email')
#       password = self.cleaned_data.get('password')
#       confirm_password = self.cleaned_data.get('confirm_password')
#       if password != confirm_password:
#           raise forms.ValidationError("Passwords do not match")
#       return confirm_password

#   def save(self, commit=True):
#       user = super(SignUpForm, self).save(commit=False)
#       user.set_password(self.cleaned_data['password'])
#       user.is_active = True

#       if commit:
#           user.save()
#       return user


#       email_qs = MyUser.objects.filter(email=email)

#       if email_qs.exists():
#           raise forms.ValidationError(
#                   "Email is already registered"
#               )
#       return email



# class UserLoginForm(forms.Form):
#   username = forms.CharField(label='Username')
#   password = forms.CharField(widget = forms.PasswordInput)

#   def clean(self, *args, **kwargs):
#       username = self.cleaned_data.get('username')
#       password = self.cleaned_data.get('password')

#       if username and password:
#           MyUser = authenticate(username= username, password=password)
#           if not MyUser:
#               raise forms.ValidationError('User does not exist')
#           if not MyUser.check_password(password):
#               raise forms.ValidationError('Incorrect password')
#       return super(UserLoginForm, self).clean(*args,**kwargs)
