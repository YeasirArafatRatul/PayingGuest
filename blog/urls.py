from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView)


urlpatterns = [
    path('rooms/', PostListView.as_view(), name='rooms'),
    path('post/new/', PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-details'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]
