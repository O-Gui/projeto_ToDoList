from django.shortcuts import render, redirect
from .models import todo
from .forms import TodoForm

def home(request):
    if request.method == 'POST':
        if 'add_task' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('home')

        elif 'complete_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = todo.objects.get(id=task_id)
            task.isCompleted = not task.isCompleted
            task.save()
            return redirect('home')

        elif 'delete_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = todo.objects.get(id=task_id)
            task.delete()
            return redirect('home')

        elif 'update_task' in request.POST:
            task_id = request.POST.get('task_id')
            new_title = request.POST.get('new_title')
            task = todo.objects.get(id=task_id)
            task.title = new_title
            task.save()
            return redirect('home')

    todos = todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

def about(request):
    context = {'name': 'Seu Nome', 'age': 25}
    return render(request, 'about.html', context)
