from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm 
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib import messages
# Create your views here.


def sign_up(request):
	if request.method == 'POST':
		fm = SignUpForm(request.POST) 
		if fm.is_valid():
			fm.save()
			messages.success(request, 'Account Created Successfully. You Can Log In Now')
			return redirect('user-login')
	else: 
		fm = SignUpForm() 
	context ={
		'signupForm': fm
	}
	return render(request, 'signup.html', context)



def user_login(request):
	if request.method == 'POST':
		fm = AuthenticationForm(request=request, data=request.POST) 
		if fm.is_valid():
			user_name = fm.cleaned_data['username']
			user_password = fm.cleaned_data['password'] 

			user = authenticate(username=user_name, password=user_password) 

			if user is not None: 
				login(request, user) 
				messages.success(request, 'Welcome to StackBlitz ERP')
				return redirect('stock-home-page')
	else:
		fm = AuthenticationForm() 
	
	context = {
		'loginForm':fm,
	}
	return render(request, 'userlogin.html', context)



def user_logout(request):
	logout(request) 
	return redirect('user-login')