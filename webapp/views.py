from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, IT_RequestForm
from. models import IT_Request
from django.http import FileResponse
import os

def unauthorized_user(request):
    return render(request, 'unauthorized.html')


def secureFile(request, file):
    
    document = get_object_or_404(IT_Request,upload="user_uploads/"+file)
    path,file_name=os.path.split(file)

    response = FileResponse(document.upload)
    if request.user.is_authenticated:
        if request.user == document.user or request.user.is_superuser:
            return response
        else:
            return redirect('unauthorized')
    else:
        messages.error(request, "You must be logged in first!")
        return redirect('login')
    
 

def home(request):
    return render(request, 'home.html')
    

def login_user(request):

    if request.user.is_authenticated:
       return HttpResponse("You are already authenticated. Please log out first.")
       

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in!")
            return redirect('viewactive', username=user.username)
        else:
            messages.error(request, "Accounts credentials invalid! Please try again or register.")
            return render(request, 'login.html')  
    else:
        return render(request, 'login.html')
    

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You Have Been Successfully Logged Out!")
        return redirect('login')
    else:
        messages.error(request, "You are not logged in. Please log in first.")
        return redirect('login')


def register_user(request):
    
    if request.user.is_authenticated:
       return HttpResponse("You are already authenticated. Please log out first.")
      
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered! Please log in.")
            return redirect('login')
		
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form': form})


def submitrequest_user(request, username=None):
    if request.user.is_authenticated:
        if request.user.username == username:
            if request.method == 'POST':
                form = IT_RequestForm(request.POST, request.FILES)
                if form.is_valid():
                    it_request = form.save(commit=False)
                    it_request.user = request.user  # Set the user field
                    it_request.save()
                    messages.warning(request, "Request submitted! Awaiting admin approval.")
                    return redirect('viewreview', username=request.user.username)

            else:
                form = IT_RequestForm()  # Create an empty form if the request is not POST
            return render(request, 'submitrequest.html', {'form': form})
        else:
            return redirect('unauthorized')
    else:
        messages.error(request, "You Must Be Logged In First!")
        return redirect('login')
	

def viewreview_user(request, username=None):
    if request.user.is_authenticated:
        if request.user.username == username:
            if request.user.is_superuser:
                it_requests = IT_Request.objects.all()
            else:
                it_requests = IT_Request.objects.filter(user=request.user)
            return render(request, 'viewreview.html', {'it_requests': it_requests})
        else:
            return redirect('unauthorized')
    else:
        messages.error(request, "You must be logged in first!")
        return redirect('login')
    

def viewactive_user(request, username=None):
    if request.user.is_authenticated:
        if request.user.username == username:
            if request.user.is_superuser:
                it_requests = IT_Request.objects.all()
            else:
                it_requests = IT_Request.objects.filter(user=request.user)
            return render(request, 'viewactive.html', {'it_requests': it_requests})
        else:
            return redirect('unauthorized')
    else:
        messages.error(request, "You must be logged in first!")
        return redirect('login')
    

def viewhistory_user(request, username=None):
    if request.user.is_authenticated:
        if request.user.username == username:
            if request.user.is_superuser:
                it_requests = IT_Request.objects.all()
            else:
                it_requests = IT_Request.objects.filter(user=request.user)
            return render(request, 'viewhistory.html', {'it_requests': it_requests})
        else:
            return redirect('unauthorized')
    else:
        messages.error(request, "You must be logged in first!")
        return redirect('login')