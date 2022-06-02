
from django import forms
from .models import *



class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee 
        fields = '__all__'
      


class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee 
        fields = '__all__'


# class AttendanceForm(forms.ModelForm):
#     class Meta: 
#         model = Attendence 
#         fields = '__all__'



class EmployeeSearchForm(forms.ModelForm):
    class Meta:
        model = Employee 
        fields = ['mobile']


