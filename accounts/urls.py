from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('products/', views.products),
  path('customer/<str:pk>/', views.customer),

  path('create_order/', views.createOrder, name="create_order"),
  path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
]
