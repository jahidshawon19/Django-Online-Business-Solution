
from django.urls import path
from stock_module import views
urlpatterns = [
 
    path('', views.stock_home_page, name='stock-home-page'),
    path('add_vendor/', views.add_vendor, name='add-vendor'),
    path('update_vendor/<str:pk>/', views.update_vendor, name='update-vendor'),
    path('deletevendor/<str:pk>/', views.delete_vendor, name='delete-vendor'),



    path('add_category/', views.add_category, name='add-category'),
    path('category/', views.category_list, name='category-list'),
    path('update_category/<str:pk>/', views.update_category, name='update-category'),
    path('deletecategory/<str:pk>/', views.delete_category, name='delete-category'),


    path('add_product/', views.add_product, name='add-product'),
    path('products/', views.product_list, name='product-list'),
    path('update_product/<str:pk>/', views.update_product, name='update-product'),
    path('delete_product/<str:pk>/', views.delete_product, name='delete-product'),
    path('product_detail/<str:pk>/', views.product_detail, name='product-detail'),



    path('issue_items/<str:pk>/', views.issue_items, name="issue-items"),
    path('receive_items/<str:pk>/', views.receive_items, name="receive-items"),


    path('history/', views.report, name='list-history'),
    
 




]
