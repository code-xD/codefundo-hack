from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VoterViewSet

router = DefaultRouter()
router.register('details', VoterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
