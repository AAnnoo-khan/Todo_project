from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'TODO item created successfully.')
            return redirect('todo_list')
    else:
        form = TodoItemForm()
    return render(request, 'todo_app/todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'TODO item updated successfully.')
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todo_app/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'TODO item deleted successfully.')
        return redirect('todo_list')
    return render(request, 'todo_app/todo_confirm_delete.html', {'todo': todo})
