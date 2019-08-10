from django.urls import path, include
from .views import EVoterFormView
urlpatterns = [
    path('', EVoterFormView),
]
