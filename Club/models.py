from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingdate = models.DateField()
    meetingtime =  models.TimeField()
    meetinglocation = models.CharField(max_length=255)
    meetingagenda = models.TextField(null=True, blank=True)

    
    def __str__(self):
        return self.meetingtitle
    
    
    class Meta():
        db_table='meeting'



class MeetingMinutes(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance = models.ManyToManyField(User)
    minutes = models.TextField()

    def __str__(self):
        return self.minutes
    
    class Meta():
        db_table='meetingminutes'


class Resource(models.Model):
    resource = models.CharField(max_length=255)
    resourcetype = models.CharField(max_length=255)
    resourceurl = models.URLField(null=True, blank=True)
    resourcedate = models.DateField()
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedesc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resource
    
    class Meta():
        db_table = 'resource'
        


class Event(models.Model):
    eventtitle = models.CharField(max_length=255)
    eventlocation = models.CharField(max_length=255)
    eventdate = models.DateField()
    eventtime = models.TimeField()
    eventdescription = models.TextField()
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)  

    def __str__(self):
        return self.eventtitle
    
    class Meta():
        db_table = 'event'
        





