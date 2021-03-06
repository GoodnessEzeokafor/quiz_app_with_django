# Generated by Django 2.0.6 on 2019-05-31 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False, verbose_name='Correct Answer')),
            ],
            options={
                'verbose_name': 'Choices',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(help_text='Category Title', max_length=255)),
                ('slug', models.SlugField(help_text='Quiz Code, should be separated by dash e.g category-code', max_length=255, unique=True, verbose_name='Quiz Code')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=4000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the quiz', max_length=255, unique=True)),
                ('slug', models.SlugField(help_text='Quiz Code, should be separated by dash', max_length=255, unique=True, verbose_name='Quiz Code')),
                ('duration', models.DurationField(blank=True, help_text='Duration Of The Quiz: HH:MM:SS or 00:00:00', max_length=255, null=True)),
                ('pass_mark', models.IntegerField(help_text='Student Pass Mark')),
                ('description', models.TextField(default='Quiz description', help_text='Description for the quiz')),
                ('publish', models.BooleanField(default=False, help_text='Tick if you want the quiz to be visible')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('take_quiz', 'Can Take Quiz'),),
                'verbose_name': 'Quiz/Exams',
                'default_permissions': ('add', 'change', 'delete'),
                'verbose_name_plural': 'Quizzes/Exams',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.Question'),
        ),
    ]
