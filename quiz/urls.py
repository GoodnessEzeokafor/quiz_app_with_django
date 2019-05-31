from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView   

app_name = 'quiz'

urlpatterns = [
 path('', views.QuizListView.as_view(),name='list'),
path('countdown/', views.countdown, name='countdown'),

#  path('list/', views.QuizListDisplayView.as_view(), name='quiz_list_detail'),
 path('create/', views.QuizCreateView.as_view(),name='create'),
 path('<slug:slug>/',views.QuizDetailView.as_view(), name='detail'),
 path('<slug:slug>/edit/', views.QuizUpdateView.as_view(), name='edit'),
 path('<slug:slug>/delete', views.QuizDeleteView.as_view(), name='delete'),
 path('<quiz_slug>/question/upload/', views.upload_question, name='upload_question'),
 path('<category_slug>/<quiz_slug>/take/', views.take_quiz, name='take_quiz'),
 path('<category_slug>/<quiz_slug>/completed/', views.quiz_completed, name='completed'),
#  path('<category_slug>/<quiz_slug>/list/', views.QuizListDisplayView.as_view(), name='quiz_list_detail'),
]






