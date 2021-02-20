from django.urls import path
from . import views

urlpatterns = [
   path('',views.index, name='index'), 
   path('Resources/', views.Resources, name='Resource'),
   path('Meetings/', views.Meetings, name='Meeting'),
   path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
   path('newMeeting/', views.newMeeting, name='newmeeting'),
   path('newResource/', views.newResource, name='newresource'),
   
]