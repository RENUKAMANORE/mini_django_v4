from django.urls import path
from .views import welcome,portal_details

urlpatterns = [
    path("",welcome),
    path("portal/",portal_details)

]
