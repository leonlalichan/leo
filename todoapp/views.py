from asyncio import tasks

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'tasks'
class Detailview(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'

class Deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url=reverse_lazy('v/')

class UpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        # Redirect to 'c' URL with the updated task's id
        return reverse_lazy('c', kwargs={'pk': self.object.id})

def task_list(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority,date=date)
        task.save()
    return render(request, "home.html", {'tasks': task1})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'POST':

        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request, id, ):
    task = Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})
        
        
