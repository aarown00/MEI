
from django.urls import path
from .import views

urlpatterns = [
   #static url route
   path('', views.home, name='home'),
   path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register/', views.register_user, name='register'),
   path('unauthorized/', views.unauthorized_user, name='unauthorized'),
  
   #dynamic url route
   path('<str:username>/submitrequest/', views.submitrequest_user, name='submitrequest'),
   path('<str:username>/viewreview/', views.viewreview_user, name='viewreview'),
   path('<str:username>/viewactive/', views.viewactive_user, name='viewactive'),
   path('<str:username>/viewhistory/', views.viewhistory_user, name='viewhistory'),

   #media route
   path("media/user_uploads/<str:file>",views.secureFile, name="securefileupload")


   
]