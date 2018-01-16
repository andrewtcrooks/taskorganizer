"""Home operations."""
from django.http import HttpResponseRedirect
from django.shortcuts import render

from tasklist.app.forms import SignupForm
from tasklist.app.models import User, Task


def main_page(request):
    """Main view."""
    if 'user_id' in request.session:
        user_obj = User.objects.filter(id=request.session['user_id'])
        task_obj = Task.objects.filter(user_id=request.session['user_id'])
        total_items = len(task_obj)
        complete_items = len(Task.objects.filter(complete=True))

        if request.method == 'POST':
            id_list = request.POST.getlist('complete')
            id_list = [int(i) for i in id_list]
            complete_items = len(id_list)

            for i in range(len(task_obj)):

                if task_obj[i].id in id_list:
                    task_obj[i].complete = True
                else:
                    task_obj[i].complete = False
                task_obj[i].save()

        incomplete_items = total_items - complete_items
        data = {'fname': request.session['first_Name'],
                'user': user_obj,
                'task': task_obj,
                'a': 0,
                'complete_items': complete_items,
                'incomplete_items': incomplete_items
                }
        return render(request, 'home.html', data)
    else:
        form = SignupForm()
        variables = {'form': form}
        return render(request, 'index.html', variables)


def signup(request):
    """Sign-up view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            obj = form.save()
            id = obj.id
            request.session['user_id'] = id
            request.session['first_Name'] = form.cleaned_data['first_Name']
    return HttpResponseRedirect('/')


def login(request):
    """Login view."""
    user_obj = User.objects.filter(email=request.POST.get('email'),
                                   password=request.POST.get('password'))
    if user_obj.count():
        print(user_obj)
        request.session['user_id'] = user_obj[0].id
        request.session['first_Name'] = user_obj[0].first_Name
    return HttpResponseRedirect('/')


def logout(request):
    """Logout view."""
    del request.session['user_id']
    del request.session['first_Name']
    request.session.modified = True
    return HttpResponseRedirect('/')
