

from django.forms import ModelForm 
from .models import * 


class OrderForm(ModelForm):
    class Meta:
        model = Order 
        fields = '__all__' 


class CreateCustomerForm(ModelForm):
    class Meta:
        model = Customer 
        fields = '__all__'

class UpdateCustomerForm(ModelForm):
    class Meta:
        model = Customer 
        fields = '__all__'