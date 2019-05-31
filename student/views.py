from django.shortcuts import render
from account.forms import UserSignUpForm
from quiz.models import Quiz
from .forms import StudentProfileCreateForm
from django.contrib.auth.models import Group
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from .models import StudentProfile
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.




@login_required(login_url='/account/login/')
@permission_required('student.add_student', raise_exception=True)
def register(request):
    '''
    register view for student profile
    adds the student to the group Student
        student is only permitted to take quiz

    return a http response redirect to /account/login

    Template: account/students/profile/create_form.html
    Context Variable: user_form, profile_form
    Request Method: POST

    '''
    if request.method == 'POST':
        user_form = UserSignUpForm(data=request.POST)
        profile_form = StudentProfileCreateForm(
            data = request.POST,
            files = request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.student = True
            user.save()
            user.groups.add(Group.objects.get(name='Student'))


            profile = profile_form.save(commit=False)
            profile.user = user # set the user created to the profile
            if 'photo' in request.FILES:
                profile.photo = request.FILES['photo']
            profile.save()
            # return HttpResponseRedirect(reverse('account:student_profile:student_detail', args=[profile.pk]))
            return HttpResponseRedirect(reverse('account:student_profile:student_list'))

            # return reverse_lazy('students_profile:student_profile_detail')

    else:
        user_form = UserSignUpForm()
        profile_form = StudentProfileCreateForm()
    return render(request,'account/students/profile/create_form.html', {
        'user_form':user_form,
        'profile_form':profile_form
    })
def upload_student(request):
    template_name ='account/student/upload.html'
    return render(request, template_name, context)


class StudentProfileDetailView(DetailView):
    model = StudentProfile
    template_name = 'account/students/detail.html'


class StudentListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = StudentProfile
    template_name = 'account/students/list.html'
    paginate_by = 10
    login_url = '/account/login/'
    permission_required = ('student.add_student','student.change_student')
    raise_exception = True

class StudentProfileUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = StudentProfile
    login_url = '/account/login/'
    permission_required = ('student.add_student','student.change_student')
    raise_exception = True



# class StudentQuizListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
#     queryset = Quiz.objects.filter(publish=True)
#     template_name = 'accuont/students/quiz/list'
#     login_url = '/account/login'
#     permission_required =('quiz.take_quiz')






class StudentQuizDetailView(DetailView):
    pass
