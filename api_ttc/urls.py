from django.urls import path
from .views import Services

urlpatterns = [
    path('', Services, name='Services'),
]