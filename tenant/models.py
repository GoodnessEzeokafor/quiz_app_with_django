# from django.db import models
# from tenant_schemas.models import TenantMixin
# # Create your models here.

# class Organisation(TenantMixin):
#     name_of_organisation = models.CharField(
#         max_length=255,
#     )
#     # company_email = models.EmailField(unique=True)
#     # phone_number = models.CharField(max_length=14)
#     # postal_code = models.CharField(max_length=7)
#     # on_trial = models.BooleanField()
#     # date_created = models.DateTimeField(
#     #     auto_now_add=True
#     # )
#     auto_create_schema=True


#     def __str__(self):
#         return self.name_of_organisation