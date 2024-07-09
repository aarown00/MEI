from django.shortcuts import redirect
from django.urls import reverse

class Redirect404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            if request.user.is_authenticated:
                username = request.user.username
                profile_url = reverse('viewprofile', kwargs={'username': username})
                return redirect(profile_url)
            else:
                login_url = reverse('login')  
                return redirect(login_url)
        return response
