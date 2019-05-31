from django.urls import path, re_path, include
from django.contrib.auth import views as auth_view
from . import views 
from profiles import views as profileviews # profile app
 
app_name = 'account'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    #signup
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('student/', include('student.urls', namespace='student_profile')),
    path('examiner/', include('examiner.urls', namespace='examiner_profile')),
    path('profile/', profileviews.dashboard, name='user_dashboard')
]


