from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def desktop(request):
    return render(request, 'desktop.html')


@csrf_protect
def login_user(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     print('Error')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/projects/')
        else:
            return HttpResponse('Username or password does not exist')
    return render(request, 'auth/login.html', context)


def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = 'unknown@gmail.com'
            user.save()
            login(request, user)
            return redirect('/projects/')
        else:
            return HttpResponse('Something went wrong...')
    return render(request, 'auth/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('desktop')
