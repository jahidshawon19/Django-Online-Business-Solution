
from django import forms
from .models import *

############## VENDOR FORM START ##########################
class CreateVendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
    


class UpdateVendorForm(forms.ModelForm):
    class Meta:
        model = Vendor 
        fields = '__all__'


class VendorSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Vendor 
        fields = ['comapny_name', 'vendor_name', 'mobile_no']

############## VENDOR FORM END ##########################






############## CATEGORY FORM START ##########################
class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category 
        fields = '__all__'



class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category 
        fields = '__all__'

############## CATEGORY FORM END ##########################








############## PRODUCT FORM START ##########################
class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Stock 
        fields = ['category', 'Product_Name', 'Quantity', 'Price']


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Stock 
        fields = ['category', 'Product_Name', 'Quantity', 'Price']



class ProductSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Stock 
        fields = ['Product_Name']
############## PRODUCT FORM END ##########################








############## IETEM ISSUE/RECEIVE FORM START ##########################
class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['Issue_Quantity', 'Issue_To']


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Receive_Quantity']

############## IETEM ISSUE/RECEIVE FORM END ##########################











############## STCOK SEARCH FORM START ##########################
class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    class Meta:
        model = Stock
        fields = ['category', 'Product_Name', 'start_date', 'end_date']

############## STCOK SEARCH FORM END ##########################



