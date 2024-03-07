from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    # path('person_list_json', person_list,name='person_list_json'),
    # path('', include('django_dyn_dt.urls')),
    path('', person_list, name='person_list'),
]