from django.urls import path,re_path
from . import views

app_name='student_profile'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student_list'),
    # path('quiz/list', views.StudentQuizListView.as_view(), name='student-quiz-list'),
    path('<int:pk>/detail/', views.StudentProfileDetailView.as_view(), name='student_detail'),
    path('<int:pk>/edit/',views.StudentProfileUpdateView.as_view(), name='student_edit'),
    path('register/', views.register, name='register'),
]

