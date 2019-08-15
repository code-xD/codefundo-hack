from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateTokenView, APIVoterLogin, APIVoterOTP, VerifyTokenView


urlpatterns = [
    # path('create/'),
    path('verify-token/', VerifyTokenView, name='verify-token'),
    path('createtoken/', CreateTokenView, name='create-token'),
    path('login/<str:token>', APIVoterLogin, name='api-login-view'),
    path('otp/<str:user>/<str:token>', APIVoterOTP, name='otp-api-view'),
    # path('addevent/'),
    # path('evoter/login/<str:token>', APIVoterLogin, name='voter-login-view')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
