from django.shortcuts import render, HttpResponse,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def hrm_home(request): #home page view
    total_employee = Employee.objects.all().count()
    total_department = Department.objects.all().count()
    salary = Employee.objects.all() 
    total_salary = sum(salary.values_list('salary', flat=True))
    last_five_employee_data = Employee.objects.order_by('id').reverse()[:5] 
    context ={
        'TotalEmployee':total_employee,
        'TotalDepartment':total_department,
        'total_salary':total_salary,
        'last_five': last_five_employee_data,
    }
    return render(request, 'hrm/dashboard.html', context)




# Employee Table List
def employee_list(request):
    employee_list = Employee.objects.all() 
    form = EmployeeSearchForm(request.POST or None)
    if request.method == 'POST':
        employee_list = Employee.objects.filter(mobile__icontains=form['mobile'].value())
    context ={
        'employee': employee_list,
        'form':form,
    }
    return render(request, 'hrm/employeeList.html', context)


def employee_details(request, id):
    single_employee = Employee.objects.get(pk=id)
    context ={
        'employee':single_employee,
    }
    return render(request, 'hrm/employeeDetails.html', context)


#create new employee 
def add_employee(request):
    form = CreateEmployeeForm() 
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST,  request.FILES) 
        if form.is_valid():
            form.save()
            messages.info(request, 'New Employee Added')
            return redirect('employee-list')
    
    context ={
        'form':form
    }
    return render(request, 'hrm/addEmployee.html', context)


def update_employee(request, id):
    update_employee = Employee.objects.get(pk=id)
    form = UpdateEmployeeForm(instance=update_employee) 
    if request.method == 'POST':
        form = UpdateEmployeeForm(request.POST, request.FILES, instance=update_employee)
        if form.is_valid():
            form.save() 
            messages.warning(request, 'Employee Information Updated Now')
            return redirect('employee-list')
    
    context = {
        'form':form, 
    }

    return render(request, 'hrm/addEmployee.html', context)


def delete_employee(request, id):
    query = Employee.objects.get(pk=id)
    if request.method == 'POST':
        query.delete() 
        messages.error(request, 'Employee Deleted From System')
        return redirect('employee-list')
    
    return render(request, 'hrm/delete.html')



def attendance(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated: 
            attend_object = Attendence(employee=request.user)
            attend_object.save()
            return redirect('attendance-list')


    return render(request, 'hrm/attendence_form.html',{})



def attendance_list(request):
    attendance = Attendence.objects.all()
  
    context ={
        'attandance':attendance,
    }

    return render(request, 'hrm/attandanceList.html', context)