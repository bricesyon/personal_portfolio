from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='index'),
    path('<int:pk>/', views.project_details, name='details'),
]
