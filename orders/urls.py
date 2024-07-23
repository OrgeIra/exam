from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:product_id>/', views.order_create, name='order_create'),
    path('', views.order_list, name='order_list'),
]
