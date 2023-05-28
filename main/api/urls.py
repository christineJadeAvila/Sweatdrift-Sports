<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('items/', views.getItems),
    path('item/<str:pk>/', views.getItem)
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('items/', views.getItems),
    path('item/<str:pk>/', views.getItem)
>>>>>>> daad950f9bf9918ace52347581126bf4060fc0af
]