from django.shortcuts import render, redirect
from django.http import HttpResponse
from sharad_app.models import Tasklist
from sharad_app.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def show_query(request):
    if request.method == "POST":
        frm = TaskForm(request.POST or None)
        if frm.is_valid():
            frm.save(commit=False).task_user = request.user
            frm.save()
        messages.success(request, "New Task Added!")
        return redirect('todo')
    else:
        all_task = Tasklist.objects.filter(task_user=request.user)
        paginator = Paginator(all_task, 4)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)
        return render (request, 'todo.html', {"all_task" : all_task})

       
def delete_entry(request, task_id):
    task = Tasklist.objects.get(pk = task_id)
    if task.task_user == request.user:
        task.delete()
        return redirect('todo')
    else:
        messages.error(request, "Sorry, You are not allowed to do that!")
        return redirect('login')

def edit_entry(request, task_id):
    if request.method == "POST":
        task = Tasklist.objects.get(pk = task_id)
        if task.task_user == request.user:
            form = TaskForm(request.POST or None, instance = task)
            if form.is_valid():
                form.save()
            messages.success(request, ("Task Edited!"))
            return redirect('todo')
        else:
            messages.error(request, "Sorry, You are not allowed to do that!")
            return redirect('login')
    else:
        task_obj = Tasklist.objects.get(pk = task_id)
        return render(request, 'edit.html', {"task_obj" : task_obj})
    
      
def done_field(request, task_id):
    task = Tasklist.objects.get(pk = task_id)
    if task.task_user == request.user:
        if not task.done:
            task.done = True
            task.save()
        else:
            task.done = False
            task.save()
        messages.success(request, ("Done Field Changed!"))
        return redirect('todo')
    else:
        messages.error(request, "Sorry, You are not allowed to do that!")
        return redirect('login')

@login_required
def show_detail(request):
    dict = {
        "text":"I am Sharad Chowdhury & my mom is a teacher.",
    }
    return render (request, 'index.html', dict)


def contact(request):
    dict = {
        "text":"This is my contact page.",
    }
    return render (request, 'contact.html', dict)


def about(request):
    dict = {
        "text":"This is my Info page.",
    }
    return render (request, 'about.html', dict)