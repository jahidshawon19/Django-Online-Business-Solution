
from django.urls import path
from inventory_module import views
urlpatterns = [
   path('inventory_module/', views.inventory_home, name='inventory-home-page'),


   path('items/', views.products, name='all-products'),
   

   path('customer/<str:pk>/', views.customer, name='customer-details'),
   path('add_customer/', views.create_customer, name='create-customer'),
   path('update_customer/<str:id>/', views.update_customer, name='update-customer'),


   path('place_order/<str:pk>/', views.create_order, name='create-order'),
   path('update_order/<str:pk>/', views.update_order, name='update-order'),
   path('delete_order/<str:pk>/', views.delete_order, name='delete-order'),


   path('customer_profile/<str:pk>/', views.customer_report, name='customer-report'),
]