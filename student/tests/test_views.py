from django.test import TestCase,RequestFactory
from django.urls import reverse
from student.models import StudentProfile
# from examiner.models import  ExaminerProfile
from django.contrib.auth.models import User 
from django.utils import timezone
from django.urls import reverse
from student.views import StudentListView

from django.contrib.auth.models import Group
# Tenants
from tenant_schemas.test.cases import TenantTestCase
from tenant_schemas.test.client import TenantClient


class StudentProfileViewsTest(TenantTestCase):
    def setUp(self):    
        self.c = TenantClient(self.tenant)
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(
            username='testuser',
            email='testuser@gmail.com',
            first_name='testuserfirstname',
            last_name='testuserlastname',
            password='secret'
        )
        cls.group = Group.objects.create(name='Student')
        cls.user.groups.add(cls.group)
        cls.user.save()

        cls.studentprofile = StudentProfile.objects.create(
            user= cls.user,
            photo = 'img.jpg',
            date_created = timezone.now(),
            date_updated =timezone.now(),
        )


class StudentProfileTestView(StudentProfileViewsTest):
    def setUp(self):
        self.c = TenantClient(self.tenant)
        self.factory = RequestFactory()


    def test_student_list_view(self):
        request = self.factory.get('/account/student/')
        response = self.c.get('/account/student/')
        self.assertEqual(response.status_code,403) # forbidden for user in group student
    
    def test_student_detail_view(self):
        request = self.factory.get('/account/student/1/detail/')
        respnonse = self.c.login('/account/student/1/detail/')
        self.assertEqual(response.status_code, 403)
    
    def test_student_register_view(self):
        # data = {
        #     'user':cls.user,
        #     'photo':'img.jpg',
        # }
        response = self.c.get('/account/student/register/')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.template, 'account/students/list.html')


        # with self.assertTemplateUsed('solos/solo_detail.html'):
        #     response.render()
        # response = StudentListView.as_view()(
        #     request,
        #     self.user
        # # )
        # self.assertEqual(response, 200)

    
    def test_student_register_view(self):
        pass
    
    def test_student_detail_view(self):
        pass
    
    def test_student_update_view(self):
        pass