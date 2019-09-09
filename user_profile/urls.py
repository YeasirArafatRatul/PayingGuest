from django.urls import path
from . import views 
# from .views import ProfileView


urlpatterns = [
	path('profile/',views.profile,name='profile'),
	path('updateprofile/',views.updateprofile,name='update_profile'),

	
]






# 	# path('', views., name = 'available-rooms'),
# 	#path('rooms/', views.rooms, name = 'available-rooms'),
# 	path('rooms/', PostListView.as_view(), name = 'rooms'),
# 	path('profile/<int:pk>/',PostDetailView.as_view(), name = 'profile'),