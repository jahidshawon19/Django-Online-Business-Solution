from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200, default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Employee(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    CITY =(
        ('Dhaka', 'Dhaka'),
        ('Chittagong', 'Chittagong'),
        ('Khulna', 'Khulna'),
        ('Sylhet', 'Sylhet'),
        ('Rajshahi', 'Rajshahi'),
        ('Mymensingh', 'Mymensingh'),
        ('Barisal', 'Barisal'),
        ('Rangpur', 'Rangpur'),
        ('Comilla', 'Comilla'),
        ('Narayanganj', 'Narayanganj'),
        ('Gazipur', 'Gazipur'),
        ('Feni', 'Feni'),
        ('Cox Bazar', 'Cox Bazar'),    
        
        )
   
    name = models.CharField(max_length=200,default='' , null=True)
    photo = models.ImageField(blank=True, upload_to='images/', default='', null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, default='')
    designation = models.CharField(max_length=200,default='', null=True)
    salary = models.IntegerField(null=True)
    gender = models.CharField(max_length=50,default='', choices=GENDER, null=True) 
    mobile = models.CharField(max_length=11, unique=True) 
    email = models.EmailField(max_length=100,unique=True)
    dob = models.DateTimeField(null=True)
    joined_on =models.DateTimeField(null=True)
    address = models.TextField(default='', null=True)
    city = models.CharField(max_length=50, choices=CITY, default='', null=True)
    

    def __str__(self):
        return str(self.name)





class Attendence(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE,default='', null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.employee.first_name