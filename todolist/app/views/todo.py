from django.http import HttpResponseRedirect
from django.shortcuts import render

from todolist.data.models import Todo


def add_todo(request):
    if request.method=='POST':
        todo_obj=Todo(todo_job=request.POST.get('job'),user_id=request.session['user_id'])
        todo_obj.save()
        return HttpResponseRedirect('/')
    else:
        data={'fname':request.session['fname']}
        return render(request,'add_todo.html',data)

def edit_todo(request,todo_id):
    if request.method=='POST':
        todo_obj=Todo.objects.filter(id=request.POST.get('id')).update(todo_job=request.POST.get('job'))
        return HttpResponseRedirect('/')
    else:
        todo_obj=Todo.objects.filter(id=todo_id)
        data={'fname':request.session['fname'],'todo':todo_obj[0]}
        return render(request,'edit_todo.html',data)

def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')