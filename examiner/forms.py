from django import forms
from .models import ExaminerProfile
# from django.contrib.auth.models import Groups



class ExaminerProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ExaminerProfile
        exclude = ('date_created', 'date_updated', 'user')

    def save(self, commit=True):
        user = super(ExaminerProfileCreateForm, self).save(commit=False)
        if commit:
            # user.student = True
            user.save()
        return user


