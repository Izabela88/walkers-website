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

handler404 = 'walkers.views.custom_page_not_found_view'
handler500 = 'walkers.views.custom_error_view'
# handler403 = 'walkers.views.custom_permission_denied_view'
# handler400 = 'walkers.views.custom_bad_request_view'