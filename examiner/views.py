from account.forms import UserSignUpForm
from .forms import ExaminerProfileCreateForm
from django.contrib.auth.models import Group
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ExaminerProfile
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.



@login_required(login_url='/account/login/')
@permission_required('examiner.add_examiner', raise_exception=True)
def register(request):
    '''
    '''
    if request.method == 'POST':
        user_form = UserSignUpForm(data=request.POST)
        profile_form = ExaminerProfileCreateForm(
            data = request.POST,
            files = request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.student = True
            user.save()
            user.groups.add(Group.objects.get(name='Examiner'))


            profile = profile_form.save(commit=False)
            profile.user = user # set the user created to the profile
            if 'photo' in request.FILES:
                profile.photo = request.FILES['photo']
            profile.save()
            return HttpResponseRedirect(reverse('account:examiner_profile:examiner_list'))
            # return reverse_lazy('students_profile:student_profile_detail')

    else:
        user_form = UserSignUpForm()
        profile_form = ExaminerProfileCreateForm()
    return render(request,'account/examiner/profile/create_form.html', {
        'user_form':user_form,
        'profile_form':profile_form
    })



def upload_examiner(request):
    template_name = 'account/examiner/upload.html'
    context = {

    }
    return render(request, template_name, context)

class ExaminerProfileDetailView(DetailView):
    model = ExaminerProfile
    template_name = 'account/examiner/detail.html'


class ExaminerListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = ExaminerProfile
    template_name = 'account/examiner/list.html'
    paginate_by = 10
    permission_required = ('examiner.add_examiner', 'examiner.change_examiner', 'examiner.delete_examiner')
    raise_exception=True

class ExaminerProfileUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = ExaminerProfile
    permission_required = ('examiner.add_examiner', 'examiner.change_examiner', 'examiner.delete_examiner')
    raise_exception=True
