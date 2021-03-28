from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
   path('',views.index, name='index'), 
   path('Resources/', views.Resources, name='Resource'),
   path('Meetings/', views.Meetings, name='Meeting'),
   path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
   path('newMeeting/', views.newMeeting, name='newmeeting'),
   path('newResource/', views.newResource, name='newresource'),
   
   path('loginmessage/', views.loginmessage, name='loginmessage'), 
   path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
   
]