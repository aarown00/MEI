from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, IT_RequestForm
from. models import IT_Request


def home(request):
    it_requests = IT_Request.objects.all()
    return render(request, 'home.html', {'it_requests': it_requests})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in!")
            return redirect('home')  
        else:
            messages.error(request, "Accounts credentials invalid! Please try again or register.")
            return render(request, 'login.html')  
    else:
        return render(request, 'login.html')
    

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Successfully Logged Out!")
    return redirect('login')


def register_user(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
		
	else:
		form = RegisterForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def notices_user(request):
    if request.user.is_authenticated:
        it_requests = IT_Request.objects.all()
        return render(request, 'notices.html', {'it_requests': it_requests})
    else:
        messages.error(request, "You must be logged in first!")
        return redirect('login')


def createrequest_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = IT_RequestForm(request.POST)
            if form.is_valid():
                it_request = form.save(commit=False)
                it_request.user = request.user  # Set the user field
                it_request.save()
                messages.success(request, "Request Submitted!")
                return redirect('home')
        else:
            form = IT_RequestForm()  # Create an empty form if the request is not POST
        return render(request, 'createrequest.html', {'form': form})
    else:
        messages.error(request, "You Must Be Logged In First!")
        return redirect('login')
	


def viewrequest_user(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            it_requests = IT_Request.objects.all()
        else:
            it_requests = IT_Request.objects.filter(user=request.user)
        return render(request, 'viewrequest.html', {'it_requests': it_requests})
    else:
        messages.error(request, "You must be logged in first!")
        return redirect('login')