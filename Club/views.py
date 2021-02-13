from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy

# Create your views here.
def index (request):
    return render(request, 'Club/index.html')

def Resources(request):
    Resource_list=Resource.objects.all()
    return render(request, 'Club/Resource.html', {'Resource_list': Resource_list})

def Meetings(request):
    Meeting_list=Meeting.objects.all()
    return render(request, 'Club/Meeting.html', {'Meeting_list': Meeting_list})

def meetingdetail (request, id):
    meet=get_object_or_404(Meeting, pk=id)
    return render (request, 'Club/meetingdetail.html', {'meet' : meet})      