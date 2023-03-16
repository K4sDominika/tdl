from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

# Create your views here.
from .models import Task


class TaskList(ListView):
    def get(self, request: HttpRequest) -> HttpResponse:
        model = Task
        context_object_name = 'tasks'

        context = {"task": Task}
        return render(request, "home.html", context=context)


class CreateTask(CreateView):
    model = Task
    template_name = 'create_task.html'
    # form_class = TaskItemCreateForm
    success_url = 'home'
    fields = ['title', 'description', 'due_date']


    def get(self, request: HttpRequest) -> HttpResponse:
        model = Task
        context_object_name = 'createTask'

        context = {"task": Task}
        return render(request=request, template_name="create_task.html")


class DeleteTask(DeleteView):
    model = Task
    template_name = 'deleteTask.html'
    success_url = 'home'

    def form_valid(self,  request: HttpRequest) -> HttpResponse:
        self.success(self.request, "The task was deleted successfully.")
        return super(DeleteTask, self).form_valid(self)


class UpdateTask(UpdateView):
    model = Task
    template_name = 'updateTask_html'
    fields = ['title', 'description', 'due_date']
    success_url = 'home'
