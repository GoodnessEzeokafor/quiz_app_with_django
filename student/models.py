from django.db import models
from django.conf import settings
from django.urls import reverse
from quiz.models import Quiz, Answer
# Create your models here.
# Create your models here.


class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        models.CASCADE
    )
    # photo = models.ImageField(
    #     upload_to = "media/student/%Y/%m/%d",
    #     blank=True,
    #     null=True
    # )
    quizzes = models.ManyToManyField(
        Quiz,
        through = 'TakenQuiz',
        blank=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        help_text = 'Format: YYYY-MM-DD'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
            help_text = 'Format: YYYY-MM-DD'
        
    )

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers.filter(answer__question__quiz=quiz).values_list('answer__question__pk',flat=True)
        questions = quiz.question_set.exclude(pk__in=answered_questions).order_by('id')
        return questions
    

    def __str__(self):
        return '%s' % self.user

    def get_absolute_url(self):
        return reverse('account:student_profile:student_detail', args=[self.id])




class TakenQuiz(models.Model):
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='taken_quizzes'
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name = 'taken_quizzes'
    )
    score = models.FloatField()
    date =models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return '{} taken by {} on {}. Score {}'.format(self.quiz, self.student, self.date, self.score)


# class TakenQuiz(models.Model):
#     student = models.ForeignKey(
#         StudentProfile,
#         on_delete=models.CASCADE,
#         related_name='taken_quizzes'
#     )
#     quiz = models.ForeignKey(
#         Quiz,
#         on_delete=models.CASCADE,
#         related_name = 'taken_quizzes'
#     )
#     score = models.FloatField()
#     date =models.DateTimeField(
#         auto_now_add=True
#     )


class StudentAnswer(models.Model):
    student = models.ForeignKey(
        StudentProfile,
        on_delete= models.CASCADE,
        related_name = 'quiz_answers'
    )
    answer = models.ForeignKey(
        Answer,
        on_delete = models.CASCADE,
        related_name='+'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{} by {} at {}'.format(self.answer, self.student, self.date_created)


# 