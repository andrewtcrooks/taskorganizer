from django.http import HttpResponseRedirect
from django.shortcuts import render

from todolist.app.forms import SignupForm
from todolist.data.models import User, Todo


def main_page(request):
    if 'user_id' in request.session:
        user_obj = User.objects.filter(id=request.session['user_id'])
        todo_obj = Todo.objects.filter(user_id=request.session['user_id'])
        for i in range(len(todo_obj)):
            print(todo_obj[i].id)
        for i in range(len(todo_obj)):
            print(todo_obj[i].complete)

        print(todo_obj)
        if request.method == 'POST':
            # get id list for boxes that are currently checked
            id_list = request.POST.getlist('complete')
            id_list = [int(i) for i in id_list]
            print(id_list)

            # zero out checkboxes to account for unchecking boxes
            for i in range(len(todo_obj)):
                todo_obj[i].complete=False
                # recheck all boxes with id in id_list
                print(todo_obj[i].id)
                if todo_obj[i].id in id_list:
                    todo_obj[i].complete=True

                todo_obj[i].save()

        data={'fname':request.session['fname'],'user':user_obj,'todo':todo_obj,'a':0}
        print('test')
        return render(request,'home.html',data)
    else:
        form = SignupForm()
        variables = {'form': form}
        return render(request,'index.html', variables)

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
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




    #if request.method == 'POST':
    #    id_list = request.POST.getlist('complete')
    #    todo_obj = Todo.objects.filter(id__in=id_list).update(complete=True)


    #todo_form = TodoForm(request.POST or None)


    #if request.method == 'POST':
    #    todo_obj = Todo(request.POST)
    #    if todo_obj.is_valid():
    #        # do something with the formset.cleaned_data
    #        todo_obj.save()
    #pass
    # else:
    #    todo_obj=Todo.objects.filter(user_id=request.session['user_id'])
    # if this is a POST request we need to process the form data
    #if request.method == 'POST':
    #    todo_form = TodoForm(request.POST or None)
    #print(request.POST)
    #completed = 'completed' in request.POST            # Have we been provided with a valid form?
    #    if todo_form.is_valid():
    #        obj = todo_form.save(commit=False)
    #        complete=request.POST.get('complete')
    #        obj.complete=complete
    #        obj.save()
    #comp =

    # This time we cannot commit straight away.
    # Not all fields are automatically populated!
    #instance = todo_form.save(commit=False)

    # Retrieve the associated model object so we can add it.
    #id = User.objects.get()
    #complete = todo_obj.objects.get(user_id=request.session['user_id'])
    #instance.complete = complete
    #instance.id=id

    # Also, create a default value for the number of views.
    #instance.views = 0

    # With this, we can then save our new model instance.
    #todo_form.user_id=user_id
    #todo_form.complete_list = complete_list
    #todo_form.save()
    #else:
    #print(todo_form.errors)
