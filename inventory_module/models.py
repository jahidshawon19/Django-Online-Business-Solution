
from pyexpat import model
from django.db import models
from stock_module.models import Stock
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)

# class Category(models.Model):

#     name = models.CharField(max_length=100) 
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


#     def __str__(self):
#         return str(self.name)

# class Product(models.Model):


#     name = models.CharField(max_length=200,)
#     price = models.FloatField(null=True)
#     category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.name)




class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out For Delivery','Out For Delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer,  on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Stock,  on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default='0')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return str(self.customer.name)