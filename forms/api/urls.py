from django.urls import path
from .views import UserRegistrationAPI, UserDetailsAPIView, UserUpdateAPIView


urlpatterns = [
    path('user/registration/', UserRegistrationAPI.as_view(), name='new-post'),
    path('user/<int:id>/details', UserDetailsAPIView.as_view(), name='post-details'),


]
