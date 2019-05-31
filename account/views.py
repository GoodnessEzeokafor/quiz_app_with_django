from django.shortcuts import render, redirect
from django.views.generic.edit import (
    CreateView
)
from .forms import UserSignUpForm,UserLoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
# Create your views here.


class SignUp(CreateView):
    template_name = 'account/signup.html'
    form_class = UserSignUpForm
    success_url = reverse_lazy('account:login')







def login_view(request):
    if request.user.is_authenticated:
        return redirect('/account/profile/')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated)
        return redirect('/account/profile/')
    template_name = 'account/login.html'
    context = {
        'form':form
    }
    return render(request, template_name, context)






