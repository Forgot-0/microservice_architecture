from django.urls import path
from .views import activation


urlpatterns = [
    path('verify/<str:uid>/<str:token>/', activation),
   
]
