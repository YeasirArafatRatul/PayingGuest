from django.urls import path
from .views import PostapiView, PostCreateView, PostUpdateAPIView, PostDetailsAPIView, PostDeleteAPIView


app_name = "blog"
urlpatterns = [
    # path('single-pair/<str:key>/', .as_view(), name='single-pair'),
    path('all-posts/', PostapiView.as_view(), name='all-posts'),
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:id>/update', PostUpdateAPIView.as_view(), name='update-post'),
    path('post/<int:id>/details', PostDetailsAPIView.as_view(), name='details-post'),
    path('post/<int:id>/delete', PostDeleteAPIView.as_view(), name='delete-post'),
]
