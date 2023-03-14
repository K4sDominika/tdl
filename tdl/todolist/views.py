from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Task
from django.views.generic.list import ListView


class TaskList(ListView):
    def get(self, request: HttpRequest) -> HttpResponse:

        model = Task
        context_object_name = 'tasks'

        context = {"task": Task}
        return render(request, "home.html", context=context)