from django.urls import path,re_path
from . import views

app_name='examiner_profile'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.ExaminerListView.as_view(), name='examiner_list'),
    path('<int:pk>/detail/', views.ExaminerProfileDetailView.as_view(), name='examiner_detail'),
    path('<int:pk>/edit/',views.ExaminerProfileUpdateView.as_view(), name='examiner_edit'),
]

