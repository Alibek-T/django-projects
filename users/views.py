from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
def get_all_users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'users.html', context=context)


def get_user_by_id(request, id):
    user = User.objects.get(id=id)
    return HttpResponse(user)
