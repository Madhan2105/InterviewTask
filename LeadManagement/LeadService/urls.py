from django.contrib import admin
from django.urls import path,include
from .views import FilterView
urlpatterns = [
    path('filter/',FilterView.as_view())
]