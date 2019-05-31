from django.db import models
from django.conf import settings
from django.urls import reverse
# from student.models import StudentProfile
from django.contrib.auth.models import User
from markdown_deux import markdown


class Category(models.Model):
    '''
    Model Name: Category
    Fields/Attributes  : category_title, slug, date_created, date_updated
            - category_title
                - the field for the category title
            - slug
                - the field for SEO url
            - date_created
                - the field that stores the date the category was created
            - date_updated
                - the field that stores the date the category was updated
    Methods: __str__
            - string representation of the model/class
            Meta:
                - verbose_name
                - verbose_name_plural

    Developer: Goodness Ezeokafor
    Date: 22nd December 2018
    '''
    category_title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text='Category Title'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        help_text = 'Quiz Code, should be separated by dash e.g category-code',
        verbose_name='Quiz Code',
    )
    date_created=models.DateTimeField(
        auto_now_add=True
    )
    date_updated=models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_title

class Quiz(models.Model):
    '''
    Model: Quiz
    fields: title,slug,user,duration,marks, pass_marks, description,category, date_created,date_upadated
          - Title : Title of the quiz
          - Slug: SEO Url
          - Duration: Stores the time duration of the quiz
          - Marks : Mars awarded to each correct answer
          - Description: Quiz Description/Procedures,Rules
          - Category: A many to one relationship with the Category table, stores the category of the quiz
          - Date Created:the field that stores the date the category was created
          - Date Updated:the field that stores the date the category was updated
          - Meta
                - verbose_name
                - verbose_name_plural
                - default_permissions: default permissions
                - permission : custom permissions
        Methods:
            __str__: string representation of the model
            get_absolute_url: redirects
    Developer:Goodness Ezeokafor
    Date: 22nd December 2018
    '''
    title = models.CharField(
        unique=True,
        max_length=255,
        blank=False,
        null=False,
        help_text = 'Title of the quiz'
    )
    slug = models.SlugField(
        unique=True,
        max_length=255,
        help_text = 'Quiz Code, should be separated by dash',
        verbose_name='Quiz Code'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    duration = models.DurationField(
        max_length=255,
        blank=True,
        null=True,
        help_text ='Duration Of The Quiz: HH:MM:SS or 00:00:00'
    )
    # marks = models.IntegerField(
    #     blank=False,
    #     null=False,
    #     help_text = 'Marks to be awarded to each question'
    # )
    pass_mark = models.IntegerField(
        blank=False,
        null=False,
        help_text = 'Student Pass Mark'
    )
    description = models.TextField(
        default='Quiz description',
        help_text = 'Description for the quiz'
        )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    publish = models.BooleanField(
        default=False,
        help_text='Tick if you want the quiz to be visible'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    date_updated = models.DateTimeField(
        auto_now=True
    )


    class Meta:
        verbose_name = 'Quiz/Exams'
        verbose_name_plural = 'Quizzes/Exams'
        default_permissions = ('add', 'change', 'delete')
        permissions =(
            ('take_quiz', 'Can Take Quiz'),
        )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quiz:detail', args = [self.slug])

    def get_take_quiz_url(self):
        return reverse('quiz:take_quiz', args=[self.category.slug, self.slug])

class Question(models.Model):
    '''
    Model Name: Question
    Fields : quiz, text, date_created, date_updated
    Methods:
         - __str_: string representation
    '''
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        # related_name = 'quest'

    )
    text = models.CharField(
        max_length=4000,
        blank=True,
        null=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ('id',)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('quiz:question_list_view')
    

    def get_markdown(self):
        text = self.text
        return markdown(text)



class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete = models.CASCADE,
        related_name = 'answers'
    )
    text= models.CharField(
        # 'Answer',
        max_length=255
    )
    is_correct = models.BooleanField(
        "Correct Answer",
        default=False
    )
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Choices'


    
    # Methods

    # def get_score_percentage(self, quiz):
    #     '''
    #     # get the quiz marks
    #     # get the quiz pass mark
    #     total_score_percent = (total_right/total_score)* 100 
    #     '''
    #     total_score_percent = (self.total_right/self.total_score) * 100
    #     return total_score_percent


