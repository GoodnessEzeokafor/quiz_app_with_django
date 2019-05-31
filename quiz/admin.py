from django.contrib import admin  # import admin functionality
from .models import Quiz,Question,Answer, Category  # from models.py
from student.models import TakenQuiz, StudentAnswer  # from the folder student
from pagedown.widgets import AdminPagedownWidget
from django.db import models


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_title',)}


class AnswerInline(admin.TabularInline):
    model = Answer
    formfield_overrides = {
        models.CharField: {'widget': AdminPagedownWidget },
    }

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': AdminPagedownWidget },
    }
    inlines = [
        AnswerInline
    ]

    list_display = ('quiz', 'text', 'date_created')
    list_filter = ('quiz',)


admin.site.register(Quiz)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)

