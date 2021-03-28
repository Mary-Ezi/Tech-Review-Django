from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.urls import reverse


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
        'resource':'Full Stack Web Developer ', 
        'resourcetype':'Online education', 
        'resourceurl':'https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/?LSNPUBID=vedj0cWlu2Y&ranEAID=vedj0cWlu2Y&ranMID=39197&ranSiteID=vedj0cWlu2Y-1943O6FpQpVyA.9CU4g5KA&utm_medium=udemyads&utm_source=aff-campaign', 
        'resourcedate':'2021-02-20',
        'resourcedesc':'This course is ', 
        'user':'self.u',
     }
    form=ResourceForm (data)
    self.assertTrue(form.is_valid)

class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.resource=Resource.objects.create(resource=' Full Stack Web Developer', 
        resourcetype='Online education',
        resourceurl='https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/?LSNPUBID=vedj0cWlu2Y&ranEAID=vedj0cWlu2Y&ranMID=39197&ranSiteID=vedj0cWlu2Y-1943O6FpQpVyA.9CU4g5KA&utm_medium=udemyads&utm_source=aff-campaign',
        resourcedate='2021-02-20', 
        resourcedesc='This course is', 
        userid=self.test_user)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login?next=/Club/newresource/')  

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newresource'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/newresource.html')      
