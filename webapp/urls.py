
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
   path('<str:username>/', views.home, name='user_home'),
   path('<str:username>/notices/', views.notices_user, name='notices'),
   path('<str:username>/createrequest/', views.createrequest_user, name='createrequest'),
   path('<str:username>/viewpending/', views.viewpending_user, name='viewpending'),
   path('<str:username>/viewapproved/', views.viewapproved_user, name='viewapproved'),
   path('<str:username>/viewcompleted/', views.viewcompleted_user, name='viewcompleted'),

   #media route
   path("media/user_uploads/<str:file>",views.secureFile, name="securefileupload")


   
]
