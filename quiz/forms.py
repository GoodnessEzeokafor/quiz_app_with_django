from django import forms
from .models import Quiz
from .models import Answer, Question
from student.models import StudentAnswer
from django.forms.utils import ValidationError
from django.db import transaction

from pagedown.widgets import PagedownWidget

class QuizCreateForm(forms.ModelForm):
    description = forms.CharField(widget=PagedownWidget)

    class Meta:
        model = Quiz
        fields = (
            'title', 
            'slug',
             'duration',
             'description',
            #   'marks',
                  'pass_mark',
              'category',
              'publish'
        )



class TakeQuizForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset = Answer.objects.none(),

        # widget = forms.SelectMultiple(),
        widget = forms.RadioSelect(),


        # widget = forms.CheckboxSelectMultiple(),
        required=True,
        empty_label=None,
        label='Choices'
    )

    class Meta:
        model = StudentAnswer
        fields = ('answer',)
    

    def __init__(self,*args, **kwargs):
        question = kwargs.pop('question') 
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answers.order_by('text')

class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get("DELETE", False):
                if form.cleaned_data.get("is_correct", False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError("Mark at least one answer as correct", code="no_correct_answer")




### Question Form






