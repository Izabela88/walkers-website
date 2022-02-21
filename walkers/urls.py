"""walkers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from walker_profile.views import ChangePasswordView, WalkerUserDelete



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('walker_profile.urls')),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
    path('<int:pk>/delete', WalkerUserDelete.as_view(), name='user_confirm_delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

