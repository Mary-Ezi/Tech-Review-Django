from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm


# Create your tests here.

class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Memory Management in Python')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Memory Management in Python')

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')  

class MeetingMinutesTest(TestCase):
    def test_string(self):
        meetingmintype = MeetingMinutes(minutes="Today")
        self.assertEqual(str(meetingmintype), meetingmintype.minutes)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def test_string(self):
        resourcetype = Resource(resource="Books")
        self.user=User(username='User1')
        self.assertEqual(str(resourcetype), resourcetype.resource)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_string(self):
        eventtype = Event(eventtitle="Intro to Python: Part 1")
        self.assertEqual(str(eventtype), eventtype.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event') 


class NewMeetingForm(TestCase):
 
 def test_meetingform(self):
    data = {
        'meetingtitle':'New meeting', 
        'meetingdate':'2021-02-20', 
        'meetingtime':'06:30:00', 
        'meetinglocation':'online',
        'meetingagenda':'First Python meeting' 
     }
    form=MeetingForm (data)
    self.assertTrue(form.is_valid)                             


class NewResourceForm(TestCase):
 #valid form data
 def test_resourceform(self):
    data = {
        'resourcename':'Full Stack Web Developer ', 
        'resourcetype':'Online education', 
        'resourceurl':'https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/?LSNPUBID=vedj0cWlu2Y&ranEAID=vedj0cWlu2Y&ranMID=39197&ranSiteID=vedj0cWlu2Y-1943O6FpQpVyA.9CU4g5KA&utm_medium=udemyads&utm_source=aff-campaign', 
        'resourcedateentered':'2021-02-20',
        'resourcedescription':'This course is designed to teach you the latest technologies for building web applications with Python 3 and Django.', 
        'user':'self.u',
     }
    form=ResourceForm (data)
    self.assertTrue(form.is_valid)
