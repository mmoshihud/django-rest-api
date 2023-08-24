from django.urls import path
from api_services.api.views import *

urlpatterns = [
    path("test", test),
]
