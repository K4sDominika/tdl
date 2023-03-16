from django.urls import path
from .views import TaskList
from .views import CreateTask
from .views import DeleteTask
from .views import UpdateTask

urlpatterns = [
    path('', TaskList.as_view(), name='task'),
    path('createTask/', CreateTask.as_view(), name='createTask'),
    path('deleteTask/', DeleteTask.as_view(), name='deleteTask'),
    path('updateTask/', UpdateTask.as_view(), name='updateTask'),
]
