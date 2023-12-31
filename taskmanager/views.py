from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import Taskform
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib import messages


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("task_list") # Redirect to the task list page
            except (IntegrityError, ValidationError) as e:
                # Handle the integrity error and provide a user-friendly message
                messages.error(request, "An error occurred: {}".format(str(e))) 
    else:
        form = Taskform()
    return render(request, 'add_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            try:
                form.save()
                return redirect("task_list") # Redirect to the task list page
            except (IntegrityError, ValidationError) as e:
                # Handle the integrity error and provide a user-friendly message
                messages.error(request, "An error occurred: {}".format(str(e))) 
    else:
        form = Taskform(instance=task)

    return render(request, 'edit_task.html', {"form":form})

def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)