from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.models import User
from .forms import ProjectForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def get_all_projects(requests):
    projects = Project.objects.all()
    return render(requests, 'projects.html', {'projects': projects})


@login_required(login_url='login')
def create_project_form(request):
    form = ProjectForm()
    return render(request, 'new_project.html', {'form': form})


@login_required(login_url='login')
def create_project(request):
    creator = User.objects.get(id=request.user.id)
    members = User.objects.get(id=request.POST.get('members', 1))
    project = Project(
        name=request.POST['name'],
        description=request.POST['description'],
        creator=creator,
        members=members,
    )
    project.save()
    return HttpResponse('Project created')


@login_required(login_url='login')
def edit_project(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'GET':
        form = ProjectForm(instance=project)
        return render(request, 'edit_project.html', {'forms': form, 'id': project.id})
    else:
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')


@login_required(login_url='login')
def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('projects')
