from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('items/', views.getItems),
    path('item/<str:pk>/', views.getItem)
]