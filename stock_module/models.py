
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vendor(models.Model):
    comapny_name = models.CharField(max_length=150)
    vendor_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    country = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.vendor_name)



class Category(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.name)



class Stock(models.Model):
    # VENDORS = (
    #     ('Tex Focus Limited', 'Tex Focus Limited'),
    #     ('Sonnet Textile', 'Sonnet Textile'),
    #     ('KDS', 'KDS'),
    # )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=50)
    Quantity = models.IntegerField(default='0')
    Price = models.IntegerField(default='0')
    Receive_Quantity = models.IntegerField(default='0')
    Receive_By = models.CharField(max_length=50)
    Issue_Quantity = models.IntegerField(default='0')
    Issue_By = models.ForeignKey(User, on_delete=models.CASCADE, default='',null=True)
    Issue_To = models.ForeignKey(Vendor, on_delete=models.CASCADE, default='',null=True)
    Phone_Number = models.CharField(max_length=50)
    Created_By = models.CharField(max_length=50)
    Reorder_Level = models.IntegerField(default='0')
    Last_Updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    Created_At = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.Product_Name)




class StockHistory(models.Model):
    VENDORS = (
        ('Tex Focus Limited', 'Tex Focus Limited'),
        ('Sonnet Textile', 'Sonnet Textile'),
        ('KDS', 'KDS'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=50)
    Quantity = models.IntegerField(default='0')
    Price = models.IntegerField(default='0')
    Receive_Quantity = models.IntegerField(default='0')
    Receive_By = models.CharField(max_length=50,)
    Issue_Quantity = models.IntegerField(default='0')
    Issue_By = models.ForeignKey(User, on_delete=models.CASCADE, default='',null=True)
    Issue_To = models.ForeignKey(Vendor, on_delete=models.CASCADE, default='',null=True)
    Phone_Number = models.CharField(max_length=50)
    Created_By = models.CharField(max_length=50)
    Reorder_Level = models.IntegerField(default='0')
    Last_Updated = models.DateTimeField(auto_now_add=False, auto_now=False)









