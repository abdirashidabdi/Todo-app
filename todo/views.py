from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def index(request):
    return render(request, 'index.html')


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo/todo.html',
                  {'all_items': all_todo_items})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


#
#
def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
