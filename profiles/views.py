from django.shortcuts import render

# Create your views here.


def dashboard(request):
    template_name = 'account/profiles/dashboard.html'
    context = {
        'dashboard':'Welcome ' + str(request.user)
    }
    return render(request, template_name, context)



#devteampassword