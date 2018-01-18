"""task operations."""
from django.http import HttpResponseRedirect
from django.shortcuts import render

from tasklist.app.models import Task


def add_task(request):
    """Add new task view."""
    if request.method == 'POST':
        task_obj = Task(task_job=request.POST.get('job'),
                        user_id=request.session['user_id'])
        task_obj.save()
        return HttpResponseRedirect('/')
    else:
        data = {'fname': request.session['first_Name']}
        return render(request, 'add_task.html', data)


def edit_task(request, task_id):
    """Edit task view."""
    if request.method == 'POST':
        task_obj = Task.objects.filter(
            id=request.POST.get('id')).update(task_job=request.POST.get('job'))
        return HttpResponseRedirect('/')
    else:
        task_obj = Task.objects.filter(id=task_id)
        data = {'fname': request.session['first_Name'], 'task': task_obj[0]}
        return render(request, 'edit_task.html', data)


def delete_task(request, task_id):
    """Delete task view."""
    Task.objects.get(id=task_id).delete()
    return HttpResponseRedirect('/')
