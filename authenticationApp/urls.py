from django.urls import path
from authenticationApp import views

urlpatterns =[
    path('signup/', views.sign_up, name='sign-up'),
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='logout'),
]