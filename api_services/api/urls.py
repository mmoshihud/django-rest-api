from django.urls import path
from api_services.api.views import *

urlpatterns = [
    path("companies/", company_list),
    path("companies/<int:pk>/", company_detail),
]
