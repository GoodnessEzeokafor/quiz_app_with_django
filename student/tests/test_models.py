from django.contrib.auth import get_user_model
from django.test import Client, TestCase,SimpleTestCase
from django.urls import reverse
from django.urls import resolve

from student.models import StudentProfile
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class StudentPofileTest(TestCase):
    def setUp(self):    
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            first_name='testfirstname',
            last_name='testlastname',
            password='secret'
        )

        self.studentprofile = StudentProfile.objects.create(
            user = self.user,
            photo = 'img.jpg',
            date_created = timezone.now(),
            date_updated =timezone.now(),
        )

    def test_studentprofile_string_representation(self):
        username = User(username='testuser')
        self.assertEqual(str(username), username.username)

    def test_studentprofile_content(self):
        self.assertEqual(f'{self.studentprofile.user}', 'testuser')
        self.assertEqual(f'{self.studentprofile.photo}', 'img.jpg')

    def test_get_absolute_url(self):
        self.assertEqual(self.studentprofile.get_absolute_url(),'/account/student/1/detail/') 
           
        # self.assertEqual(f'{self.studentprofile.date_created}','2018-12-30 07:01:54.719169+00:00')
        # self.assertEqual(f'{self.studentprofile.date_updated}','2018-12-30 07:01:54.719169+00:00')
        # self.assertEqual(f'{self.studentprofile.date_created}', timez.now())
        # self.assertEqual(f'{self.studentprofile.date_updated}', datetime.now())



