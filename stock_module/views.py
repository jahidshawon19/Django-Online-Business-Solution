
from django.shortcuts import redirect, render
from .forms import * 
from .models import *
from django.http import HttpResponse
from django.contrib import messages
import csv


# Create your views here.


def index_page(request):
	if request.user.is_authenticated:
		return render(request, 'index.html', {'name':request.user})
	else:
		return redirect('user-login')

    	


def stock_home_page(request):
	if request.user.is_authenticated:

		labels = []
		data = []
		all_vendors = Vendor.objects.all()
		all_categories = Category.objects.all()
		all_products = Stock.objects.all()
		total_vendors = all_vendors.count()
		total_category = all_categories.count()
		total_product = all_products.count()
		for vendor_data in all_vendors:
			labels.append(vendor_data.comapny_name)
			data.append(vendor_data.country)
		form = VendorSearchForm(request.POST or None)
		if request.method == 'POST':
			all_vendors = Vendor.objects.filter(comapny_name__icontains=form['comapny_name'].value(), vendor_name__icontains=form['vendor_name'].value(), mobile_no__icontains=form['mobile_no'].value())


			
			if form['export_to_CSV'].value() == True:
				response = HttpResponse(content_type='text/csv')
				response['Content-Disposition'] = 'attachment; filename="List of Vendors.csv"'
				writer = csv.writer(response)
				writer.writerow(['Company Name', 'Vendor Name', 'Mobile', 'City', 'Zipcode', 'Country', 'Created Date'])
				instance = all_vendors 
				for vendor in instance:
					writer.writerow([vendor.comapny_name,vendor.vendor_name,vendor.mobile_no, vendor.city, vendor.zip_code, vendor.country, vendor.created_at])
				return response

		context = {
			'form':form,
			'all_vendors':all_vendors,
			'total_vendors':total_vendors,
			'total_category':total_category,
			'total_product': total_product,
			'labels':labels,
			'data':data,
		
		}

		return render(request, 'stock/stock_homepage.html', context)
	else:
		return redirect('user-login')



def add_vendor(request):
	if request.user.is_authenticated:

		form = CreateVendorForm()
		if request.method == 'POST':
			form = CreateVendorForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, 'Vendor Added Successfully')
				return redirect('stock-home-page')
		context = {'form':form}
		return render(request, 'stock/add_vendor.html', context)
	else:
		return redirect('user-login')


def update_vendor(request, pk):
	if request.user.is_authenticated:

		query = Vendor.objects.get(id=pk)
		form = UpdateVendorForm(instance=query)
		if request.method == 'POST':
			form = UpdateVendorForm(request.POST, instance=query)
			if form.is_valid():
				form.save()
				messages.success(request, 'Vendor Updated Successfully')
				return redirect('stock-home-page')
	
		context = {
			'form':form
		}

		return render(request, 'stock/add_vendor.html', context)
	else:
		return redirect('user-login')

def delete_vendor(request, pk):
	if request.user.is_authenticated:

		query = Vendor.objects.get(id=pk)
		if request.method == 'POST':
			query.delete()
			messages.warning(request, 'Vendor Deleted From Table')
			return redirect('stock-home-page')
		return render (request, 'stock/delete.html')
	else:
		return redirect('user-login')



def add_category(request):
	if request.user.is_authenticated:

		form = CreateCategoryForm()
		if request.method == 'POST':
			form = 	form = CreateCategoryForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, 'Category Added Successfully')
				return redirect('category-list')
		context = {'form':form}
		return render(request, 'stock/add_category.html', context)
	else:
		return redirect('user-login')


def category_list(request):
	if request.user.is_authenticated:

		query = Category.objects.all()
		context = {
			'query':query
		}

		return render(request, 'stock/category_list.html', context)
	else:
		return redirect('user-login')


def update_category(request, pk):
	query = Category.objects.get(id=pk)
	form = UpdateCategoryForm(instance=query)
	if request.method == 'POST':
		form = UpdateCategoryForm(request.POST, instance=query)
		if form.is_valid():
			form.save()
			messages.success(request, 'Category Updated Successfully')
			return redirect('category-list')
	
	context = {
		'form':form
	}

	return render(request, 'stock/add_category.html', context)



def delete_category(request, pk):
	query = Category.objects.get(id=pk)
	if request.method == 'POST':
		query.delete()
		messages.warning(request, 'Category Deleted From Table')
		return redirect('category-list')
	return render (request, 'stock/delete.html')







def product_list(request):
	query = Stock.objects.all()
	form = ProductSearchForm(request.POST or None)
	if request.method == 'POST':
		query = Stock.objects.filter(Product_Name__icontains=form['Product_Name'].value())


		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="List of Products.csv"'
			writer = csv.writer(response)
			writer.writerow(['Product Name', 'Category', 'Total Amount', 'Created Time', 'Last Updated Time'])
			instance = query 
			for product in instance:
				writer.writerow([product.Product_Name,product.category,product.Quantity,product.Created_At, product.Last_Updated])
			return response
	context = {
		'query':query,
		'form':form,
	}

	return render(request, 'stock/item_list.html', context)


def add_product(request):
	form = ProductCreateForm(request.POST or None) 
	if form.is_valid():
		form.save()
		messages.success(request, 'New Product Added Successfully')
		return redirect('product-list')
	
	context = {
		'form':form,
	}

	return render(request, 'stock/add_item.html', context)


def update_product(request, pk):
	query = Stock.objects.get(id=pk)
	form = UpdateProductForm(instance=query)
	if request.method == 'POST':
		form = UpdateProductForm(request.POST, instance=query)
		if form.is_valid():
			form.save()
			messages.success(request, 'Product Updated Successfully')
			return redirect('product-list')
	
	context = {
		'form':form
	}

	return render(request, 'stock/add_item.html', context)




def delete_product(request, pk):
	query = Stock.objects.get(id=pk)
	if request.method == 'POST':
		query.delete()
		messages.warning(request, 'Product Deleted From Table')
		return redirect('product-list')
	return render (request, 'stock/delete.html')



def product_detail(request, pk):
    queryset = Stock.objects.get(id=pk)
    context ={
        "title":queryset.Product_Name,
        "queryset":queryset
    }
    return render(request, "stock/item_details.html", context)




def issue_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		if instance.Quantity > 0 and instance.Quantity >= instance.Issue_Quantity: 
			instance.Quantity = instance.Quantity - instance.Issue_Quantity
			messages.success(request, "Issued SUCCESSFULLY. " + str(instance.Quantity) + " " + str(instance.Product_Name) + "s now left in Store")
			instance.save()
			issue_history = StockHistory(
				id=instance.id,
				Last_Updated=instance.Last_Updated,
				category_id = instance.category_id,
				Product_Name = instance.Product_Name,
				Quantity = instance.Quantity,
				Issue_To = instance.Issue_To,
				Issue_By = instance.Issue_By,
				Issue_Quantity = instance.Issue_Quantity,
			)
			issue_history.save()
			return redirect('/product_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		
		"queryset": queryset,
		"form": form,
		
	}
	return render(request, 'stock/add_item.html', context)



def receive_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.Quantity += instance.Receive_Quantity
		instance.save()
		issue_history = StockHistory(
			id = instance.id,
			Last_Updated = instance.Last_Updated,
			category_id = instance.category_id,
			Product_Name = instance.Product_Name,
			Quantity = instance.Quantity,
			Receive_Quantity = instance.Receive_Quantity,
			Receive_By = instance.Receive_By,		
			)
		issue_history.save()

		messages.success(request, "Received SUCCESSFULLY. " + str(instance.Quantity) + " " + str(instance.Product_Name)+"s now in Store")

		return redirect('/product_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title": 'Reaceive ' + str(queryset.Product_Name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, 'stock/add_item.html', context)



def report(request):
	queryset = StockHistory.objects.all()
	form = StockSearchForm(request.POST or None)
	if request.method == 'POST':
		category = form['category'].value()
		# queryset = StockHistory.objects.filter(Product_Name__icontains=form['Product_Name'].value(),
		# 	Last_Updated__range=[form['start_date'].value(), form['end_date'].value()] )

		if category != '':
			queryset = queryset.filter(category_id=category)
		


		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="Report.csv"'
			writer = csv.writer(response)
			writer.writerow(['Category', 'Product Name', 'Quantity', 'No of Issue Item', 'Issue To', 'No of Receive Item', 'Last Updated '])
			instance = queryset 
			for item in instance:
				writer.writerow([item.category,item.Product_Name,item.Quantity, item.Issue_Quantity, item.Issue_To, item.Receive_Quantity, item.Last_Updated])
			return response
		


	context = {
		"queryset": queryset,
		"form":form,
	}

	return render(request, 'stock/report_list.html', context)





