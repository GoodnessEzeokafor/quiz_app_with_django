from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.views.generic import DetailView,ListView
from .models import Quiz,Question,Category,Answer
from student.models import StudentProfile
from django.urls import reverse_lazy
from .forms import QuizCreateForm, TakeQuizForm
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.db.models import Q
from django.db import transaction
from student.models import TakenQuiz
from django.forms.utils import ValidationError
from time import localtime, strftime, sleep
import time

# email
from django.core.mail import send_mail


class QuizCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    '''
    Class Based View
        - for creating quiz
        - permission is required
    '''
    model = Quiz
    form_class = QuizCreateForm
    # success_url = reverse_lazy('quiz:detail') get_absolute_url defined in the model
    template_name = 'quiz/form.html'
    login_url = '/account/login/'
    permission_required = ('quiz.add_quiz', 'quiz.Add_quiz')
    raise_exception = True
    

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QuizDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    '''
    Class Based View
        - for the detail
        - permission is required
    '''
    model = Quiz
    template_name = 'quiz/detail.html'
    slug_field = 'slug__iexact'  # slug field
    login_url = '/account/login/'
    permission_required = ('quiz.take_quiz')
    raise_exception = True
    

class QuizUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    '''
    Class Based View
        - for updating the quiz view
        - permission is required
    '''
    model = Quiz
    form_class = QuizCreateForm
    template_name = 'quiz/form.html'
    slug_field = 'slug__iexact'  # slug field
    login_url = '/account/login/'
    permission_required = ('quiz.add_quiz', 'quiz.delete_quiz', 'quiz.change_quiz')
    raise_exception = True
    
    def get_success_url(self):
        return reverse_lazy('quiz:detail', args=[self.object.slug])


class QuizDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    '''
    Cass Based View
        - for deleting quiz
        - permission is required
        - 
    '''
    model = Quiz
    template_name = 'quiz/quiz_confirm_delete.html'
    login_url = '/account/login/'
    permission_required = ('quiz.add_quiz', 'quiz.delete_quiz', 'quiz.change_quiz')
    raise_exception = True

    def get_success_url(self):
        '''
        Method that defines where this view will be redirected to 
        '''
        return reverse_lazy('quiz:list')



class QuizListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    '''
    Class Based View
        - for listing view

    '''
    model = Quiz
    # queryset = Quiz.objects.filter(user=request.user)
    template_name = 'quiz/quiz_list.html'
    login_url = '/account/login/'
    permission_required = ('quiz.take_quiz')
    raise_exception = True
    
    def get_queryset(self):
        return super(QuizListView,self).get_queryset().filter(Q(user=self.request.user) | Q(publish=True))




@permission_required('quiz.add_question', raise_exception=True)
def upload_question(request,quiz_slug=None):
    '''
    View for uploading the question
    '''
    quiz = get_object_or_404(Quiz,slug=quiz_slug)
    template_name = 'question/upload_question.html'
    if request.method == 'POST':
        csvfile = request.FILES['questionfile']  # gets the input field name
        print(csvfile.name)  # prints the csv file name
        if not csvfile.name.endswith('.csv'):
            print("Invalid!!") # prints invalid at the console
            messages.errors(request, "CSV file format not supported")
            return(HttpResponseRedirect('quiz:fail'))
        file_data = csvfile.read().decode("utf-8")  # reads the csv file
        # print(file_data)
        lines = file_data.split("\n") # split using the delimiter
        data_dict = {} # empty dictionary to store the csv data
        print(len(lines))
        for line in lines:
            print(line)
            fields = line.split(',')
            # print(fields)
            data_dict = {
                'question_text':fields[0],
            }
            # print(len(data_dict))
            if data_dict != '':
                question = Question.objects.create(
                    quiz=quiz,
                    text=data_dict['question_text']
                )
                # question.quiz = quiz
                # question.date_created = timezone.now()
                # question.date_upadated= timezone.now()
                # question.save()
                messages.success(request, "File Successfully Uploaded")
                # return HttpResponseRedirect(reverse('quiz:upload_successful'))
            else:
                messages.errors(request, "File not uploaded")
    context = {'quiz':quiz}
    return render(request, template_name, context)



@login_required(login_url='/account/login/')
@permission_required('quiz.take_quiz', raise_exception=True)
def take_quiz(request, category_slug=None,quiz_slug=None):
    question_no = 0
    quiz = get_object_or_404(Quiz,slug=quiz_slug)
    category = get_object_or_404(Category,slug=category_slug)
    try:
        student = StudentProfile.objects.get(user=request.user)
    except:
        raise Http404("You Can't take quiz!!.Please contact your invigilator!!")

    context = {}
    if student.quizzes.filter(slug=quiz_slug).exists():
        '''
            if the student has taken the quiz 
            redirects him/her to the taken_quiz view 
        '''
        raise Http404("You have already taken the quiz!!")
        # return render(request, 'quiz/taken_quiz.html')

    print(student)
    total_questions = quiz.question_set.count()
    unanswered_questions = student.get_unanswered_questions(quiz)  # gets the total unanwered questions
    total_unanswered_questions = unanswered_questions.count()  # counts the total unanswered questions
    try :
        progress = 100 - round(((total_unanswered_questions - 1) / total_questions) * 100) # remeber to catch the Division By Zero error
        print(progress)
    except ZeroDivisionError:
        raise ValidationError("An Issue Has Occured, Please Inform Your Invigilator!!")
    question = unanswered_questions.first()  # gets the first questioin
    if request.method == 'POST':
        form = TakeQuizForm(question=question, data=request.POST)
        question_no += 1
        if form.is_valid():
            print(question_no)
            with transaction.atomic():    
                student_answer = form.save(commit=False) # create a false commit
                student_answer.student = student # sets the currently logged in user
                student_answer.save() # saves to the the Student
                if student.get_unanswered_questions(quiz).exists():
                    # return render(request, 'quiz/take_quiz.html', {'question_no':question_no})
                    return redirect("quiz:take_quiz", category_slug, quiz_slug)
                else:
                    correct_answers = student.quiz_answers.filter(answer__question__quiz=quiz,answer__is_correct=True).count()
                    print(correct_answers)
                    score = round((correct_answers/total_questions) * 100.0, 2)
                    TakenQuiz.objects.create(
                        student=student,
                        quiz=quiz,
                        score=score
                    )
                    if score <  quiz.pass_mark:
                        # messages.warning(request, 'Sorry!!')
                        messages.warning(request, 'Better luck next time! Your score for the quiz %s was %s.' % (quiz.title, score))

                    else:
                        # messages.success(request, 'Congratulations!!!')
                        messages.success(request, 'Congratulations! You completed the quiz %s with success! You scored %s points.' % (quiz.title, score))

                    return redirect('quiz:completed', category_slug, quiz_slug)
    else:
        form = TakeQuizForm(question=question)
    # for i  in range(total_questions):
    #     question_no = i
    return render(request, 'quiz/take_quiz.html',{
        'quiz':quiz,
        'question':question,
        'form':form,
        'progress':progress,
        'total_questions':range(1,total_questions+1),
        'question_no':question_no
    })


def quiz_completed(request, category_slug, quiz_slug):
    username = request.user.username  # get the current user username
    user = User.objects.get(username=username)  # gets the current user
    student = StudentProfile.objects.get(user=request.user)  # gets the user student rofile
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    #email
    # student_email = user.email  # the user email
    # examiner_email = 'gootech442@gmail.com'  # examiner email
    # subject_email = "ISEP CBT QUIZ"
    student_quiz_result = TakenQuiz.objects.get(student=student)
    # print(type(quiz.pass_mark))
    # print(type(student_quiz_result.score))
    # if student_quiz_result.score >= quiz.pass_mark:
    #     messages.success(request, 'Congratulations! ')
    # else:
    #     messages.error(request, "Sorry!!")
    # message = "Your Result Score {}".format(student_quiz_result.score)
    # print(student_email)

    # if subject_email:
    #     send_mail(subject_email, message, examiner_email, [student_email])
    template_name = 'quiz/completed.html'
    context = {
        # "msg_1":"Weldone",
        # "student":student_email,
        # 'stud':student_quiz_result,
        # "message":message

    }
    return render(request, template_name, context)
    
    

def countdown(request):
    start_time = time.time()
    struct = localtime(start_time)

    print("\nStart Countdown At: ", strftime("%X", struct))

    i = 10
    while i > -1:
        print(i)
        i -= 1
        sleep(1)

    end_time = time.time()

    difference = round(end_time - start_time)
    print("\nRuntime", difference, "seconds")

    return HttpResponse(strftime("%X", struct))

class CategoryCreateView(CreateView):
    model = Category
    fields = ['category_title', 'category_slug']
    template_name ='quiz/category/form.html'



