from django.shortcuts import render, HttpResponseRedirect
from .forms import TaskForm
from .models import Task, Status


def index(request):
    return render(request, 'todo_app/index.html', {"tasks": Task.objects.all()})


def status(request, status_id):
    return render(request, 'todo_app/statuses.html', {"statuses": Status.objects.all()})


def task(request, task_id):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = TaskForm()

    return render(request, 'todo_app/task.html', {'form': form})
