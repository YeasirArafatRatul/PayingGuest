from django.urls import path
from .views import PostapiView, PostCreateView

app_name = "blog"
urlpatterns = [
    # path('single-pair/<str:key>/', .as_view(), name='single-pair'),
    path('all-posts/', PostapiView.as_view(), name='all-posts'),
    path('create/', PostCreateView.as_view(), name='create-post'),
]
