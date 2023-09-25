from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import Taskform

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
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
            form.save()
            return redirect("task_list") # Redirect to the task list page
        
    else:
        form = Taskform(instance=task)

    return render(request, 'edit_task.html', {"form":form})