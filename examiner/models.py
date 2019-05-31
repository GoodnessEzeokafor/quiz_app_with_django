from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.


class ExaminerProfile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE
    )
    # photo = models.ImageField(
    #     upload_to = "media/examiner/%Y/%m/%d",
    #     blank=True,
    #     null=True
    # )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return '%s' % self.user
        


    def get_absolute_url(self):
        return reverse('account:examiner_profile:examiner_detail', args=[self.id])



    