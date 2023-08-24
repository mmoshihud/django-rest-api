from django.urls import path
from api_services.api.views import *

urlpatterns = [
    path("companies/", company_list),
    path("companies/<int:pk>/", company_detail),
    path("employees/", employee_list),
    path("employees/<int:pk>/", employee_detail),
]
