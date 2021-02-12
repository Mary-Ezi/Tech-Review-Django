from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'Club/index.html')

def Resources(request):
    Resource_list=Resource.objects.all()
    return render(request, 'Club/Resource.html', {'Resource_list': Resource_list})