from django.http import HttpResponseRedirect
from django.shortcuts import render

from todolist.app.forms import SignupForm
from todolist.data.models import User, Todo


def main_page(request):
    if 'user_id' in request.session:
        user_obj=User.objects.filter(id=request.session['user_id'])
        todo_obj=Todo.objects.filter(user_id=request.session['user_id'])
        data={'fname':request.session['fname'],'user':user_obj,'todo':todo_obj,'a':0}
        return render(request,'home.html',data)
    else:
        form = SignupForm()
        variables = {'form': form}
        return render(request,'index.html', variables)

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():


            obj=form.save(commit=False)

            obj.save()


            obj=form.save()
            id=obj.id
            request.session['user_id']=id
            request.session['fname']=form.cleaned_data['fname']
    return HttpResponseRedirect('/')

def login(request):
    user_obj=User.objects.filter(email=request.POST.get('email'),password=request.POST.get('password'))
    if user_obj.count():
        print(user_obj)
        request.session['user_id']=user_obj[0].id
        request.session['fname']=user_obj[0].fname
    return HttpResponseRedirect('/')

def logout(request):
    del request.session['user_id']
    del request.session['fname']
    request.session.modified=True
    return HttpResponseRedirect('/')