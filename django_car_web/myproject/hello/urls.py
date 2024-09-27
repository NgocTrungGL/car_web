from django.urls import path # type: ignore
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
]
