from django.contrib import admin
from student.models import StudentProfile
from examiner.models import ExaminerProfile
# Register your models here.


admin.site.register(StudentProfile)
admin.site.register(ExaminerProfile)


