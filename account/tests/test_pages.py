from django.test import SimpleTestCase, TestCase
from tenant_schemas.test.cases import TenantTestCase
from tenant_schemas.test.client import TenantClient



# class AccountTestCase(TestCase):
#     def test_account_home_page_status_code(self):
#         response = self.client.get('/account/login/')
#         print(response)
#         self.assertEqual(response.status_code, 200)

class BaseSetup(TenantTestCase):
    def setUp(self):
        self.c = TenantClient(self.tenant)

    # def test_user_profile_view(self):
    #     response = self.c.get(reverse('user_profile'))
    #     self.assertEqual(response.status_code, 200)
