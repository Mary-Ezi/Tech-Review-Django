from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Meeting, MeetingMinutes, Resource, Event


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

