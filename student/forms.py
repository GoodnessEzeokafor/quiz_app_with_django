from django import forms
from .models import StudentProfile
# from django.contrib.auth.models import Groups



class StudentProfileCreateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ('date_created', 'date_updated', 'user')

    def save(self, commit=True):
        user = super(StudentProfileCreateForm, self).save(commit=False)
        if commit:
            # user.student = True
            user.save()
        return user