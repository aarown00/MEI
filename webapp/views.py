from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, IT_RequestForm
from. models import IT_Request
from django.http import FileResponse
from django.urls import reverse
import os
from django.core.mail import send_mail, BadHeaderError

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




def profile_user(request, username=None):
    if request.user.is_authenticated:
        if request.user.username == username:
            return render(request, 'profile.html')
        else:
            return redirect('unauthorized')
    else:
        messages.error(request, "You must be logged in first!")
        return redirect(reverse('login'))  # Redirect to the login URL



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
            messages.success(request, f"You have been successfully logged in, Welcome {user.first_name}!")
            return redirect('viewreview', username=user.username)
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
                    # Send email (attempt)
                    try:
                        send_mail(
                            f"IT Request - Reference RTN#{it_request.id}",  # subject
                            f"Request submitted! Your reference is RTN#{it_request.id}.\n\nPlease do not reply to this email.",  # message
                            'meitrequestsystem@gmail.com',  # from email
                            [request.user.email],  # to email
                        )
                    except BadHeaderError:
                        pass  # Invalid header error; ignore and continue
                    except Exception as e:
                        messages.warning(request, "Failed to send RTN# to email. Contact admin for support. Please check table for RTN# instead.")

                    messages.warning(request, f"Request submitted! Please wait for admin approval. Your reference is RTN#{it_request.id}.")
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
                it_requests = IT_Request.objects.all().order_by('-requested_at')
            else:
                it_requests = IT_Request.objects.filter(user=request.user).order_by('-requested_at')
            return render(request, 'viewreview.html', {'it_requests': it_requests})
        else:
            return redirect('unauthorized')
    else:
        messages.error(request, "You must be logged in first!")
        return redirect('login')
    
 

def viewhistory_user(request, username=None):
    if request.user.is_authenticated:
        if request.user.username == username:
            if request.user.is_superuser:
                it_requests = IT_Request.objects.all().order_by('-requested_at')
            else:
                it_requests = IT_Request.objects.filter(user=request.user).order_by('-requested_at')
            return render(request, 'viewhistory.html', {'it_requests': it_requests})
        else:
            return redirect('unauthorized')
    else:
        messages.error(request, "You must be logged in first!")
        return redirect('login')
    

def cancelrequest_user(request, pk):
    print(f"Cancel request received for pk={pk}")  # Debug statement
    it_request = get_object_or_404(IT_Request, pk=pk)
    # Check if the user is the owner or a superuser
    if request.user == it_request.user or request.user.is_superuser:
        if it_request.status == 'Waiting':
            it_request.status = 'Cancelled'
            it_request.save()
            messages.warning(request, f"RTN#{it_request.id} is cancelled and has been moved to history.")
        else:
            return HttpResponse("Request cannot be cancelled.")
    else:
        return HttpResponse("You are not authorized to perform this action.")
    
    return redirect('viewreview', username=request.user.username)


def approverequest_user(request, pk):
    print(f"Approve request received for pk={pk}")  # Debug statement
    it_request = get_object_or_404(IT_Request, pk=pk)
    # Check if the user is a superuser
    if request.user.is_superuser:
        if it_request.status == 'Waiting':
            it_request.status = 'Pending'
            it_request.save()
            messages.success(request, f"RTN#{it_request.id} is approved. Status is now changed to (Pending)")
  
        else:
            return HttpResponse("Request cannot be approved.")
    else:
        return HttpResponse("You are not authorized to perform this action.")
    
    return redirect('viewreview', username=request.user.username)

def donerequest_user(request, pk):
    print(f"Complete request received for pk={pk}")  # Debug statement
    it_request = get_object_or_404(IT_Request, pk=pk)
    # Check if the user is the owner or a superuser
    if request.user.is_superuser:
        if it_request.status == 'Pending':
            it_request.status = 'Completed'
            it_request.save()
            messages.success(request, f"RTN#{it_request.id} is now marked as done. Status is now changed to (Completed)")
        else:
            return HttpResponse("Request cannot be updated.")
    else:
        return HttpResponse("You are not authorized to perform this action.")
    
    return redirect('viewreview', username=request.user.username)



def closerequest_user(request, pk):
    print(f"Closed request received for pk={pk}")  # Debug statement
    it_request = get_object_or_404(IT_Request, pk=pk)
    # Check if the user is the owner or a superuser
    if request.user == it_request.user or request.user.is_superuser:
        if it_request.status == 'Completed':
            it_request.status = 'Closed'
            it_request.save()
            messages.success(request, f"RTN#{it_request.id} is closed and has been moved to history.")
        else:
            return HttpResponse("Request cannot be closed.")
    else:
        return HttpResponse("You are not authorized to perform this action.")
    
    return redirect('viewreview', username=request.user.username)
