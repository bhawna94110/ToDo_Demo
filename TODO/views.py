from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    todos = todo.objects.all()
    form = TaskForm()
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'todos':todos, 'form':form}
    return render(request, 'todo/list.html', context)

def updateTask(request, pk):
    todos = todo.objects.get(id=pk)
    return redirect(request, 'todo/update_task.html')
