from django.contrib import admin
from django.urls import path, include
from app1.views import home_view, Register, Login, profile_view, profile_update
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('signup/', Register.as_view(), name="signup"),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('accounts/logout', include('django.contrib.auth.urls'), name='logout'),
    path('accounts/profile/', profile_view, name="profile"),
    path('accounts/profile/update', profile_update, name="profileupdate"),
]

