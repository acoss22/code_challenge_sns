from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("due_date")
    return render(request, "tasks/task_list.html", {"tasks": tasks})

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task-list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form})

@login_required
def task_edit(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task-list")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_form.html", {"form": form})

@login_required
def task_delete(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("task-list")

    return render(request, "tasks/task_confirm_delete.html", {"task": task})
