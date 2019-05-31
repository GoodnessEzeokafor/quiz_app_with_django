from .models import Quiz
from django.shortcuts import get_object_or_404


def quizslug(request):
    quiz = get_object_or_404(Quiz)
    return{
        'quiz_slug':quiz,
    }
    