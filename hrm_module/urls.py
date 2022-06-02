from django.urls import path
from hrm_module import views
urlpatterns = [
    path('hrm_module/', views.hrm_home, name='hrm-home'),
    path('employee/', views.employee_list, name='employee-list'),
    path('employee/<str:id>/', views.employee_details, name='employee-details'),
    path('add_employee/', views.add_employee, name='add-employee'),
    path('update_employee/<str:id>/', views.update_employee, name='update-employee'),
    path('delete_employee/<str:id>/', views.delete_employee, name='delete-employee'),

    path('attendance/', views.attendance, name='attendance'),
    path('attendance_list/', views.attendance_list, name='attendance-list'),
]