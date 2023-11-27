from django.urls import path
from . import views

urlpatterns = [
    path('empgenfilter/', views.EmpFilter.as_view()),
]