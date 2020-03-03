
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from user_profile import views as profile_views
from forms.views import RegisterView
from forms.views import updateprofile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='forms/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='forms/logout.html'), name='logout'),
    path('profile/', profile_views.profile, name='profile'),
    path('updateprofile/', updateprofile, name='update_profile'),

    # apis
    path('blog-api/', include('blog.api.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


# path('login/', LoginView.as_view(), name = 'login'),
# path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
# path(' ',include('user_profile.urls')),
# path('accounts/',include('forms.urls')),
#path('logout/',logout.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
# path('',include('user_profile.urls')),
# path('profile/<int:pk>/', ProfileView.as_view(template_name='UserProfile.html'), name = 'profile'),
# (?P<pk>\d+)
# path('rooms/', views.rooms,name='rooms'),
