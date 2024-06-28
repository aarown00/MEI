
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
   path('<str:username>/viewhistory/', views.viewhistory_user, name='viewhistory'),
   path('<str:username>/profile/', views.profile_user, name='viewprofile'),
   
   #update status for admin only
   path('it_request/<int:pk>/approve/', views.approverequest_user, name='approverequest_user'),
   path('it_request/<int:pk>/done/', views.donerequest_user, name='donerequest_user'),

   #update for employee and admin
   path('it_request/<int:pk>/close/admin/', views.closerequest_admin, name='closerequest_admin'),
   path('it_request/<int:pk>/close/employee/', views.closerequest_employee, name='closerequest_employee'),
   path('it_request/<int:pk>/cancel/admin/', views.cancelrequest_admin, name='cancelrequest_admin'),
   path('it_request/<int:pk>/cancel/employee/', views.cancelrequest_employee, name='cancelrequest_employee'),

   #media route
   path("media/user_uploads/<str:file>",views.secureFile, name="securefileupload")


   
]