from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import loginView, OTPview, AdminLoginView, AdminProfileView

urlpatterns = [
    path('login', loginView, name='main-login-view'),
    path('otp/<slug:user>', OTPview, name='otp-login-view'),
    path('admin/login', AdminLoginView, name='admin-login-view'),
    path('admin/profile', AdminProfileView, name='admin-profile-view')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
