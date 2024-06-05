
from django.urls import path
from .import views

urlpatterns = [
   path('', views.home, name='home'),
   path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register/', views.register_user, name='register'),
   path('notices/', views.notices_user, name='notices'),
   path('createrequest/', views.createrequest_user, name='createrequest'),
   path('viewrequest/', views.viewrequest_user, name='viewrequest')

   
]
