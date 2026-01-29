from django.urls import path
from .views import task_list, task_create, task_edit, task_delete

urlpatterns = [
    path("", task_list, name="task-list"),
    path("create/", task_create, name="task-create"),
    path("<int:pk>/edit/", task_edit, name="task-edit"),
    path("<int:pk>/delete/", task_delete, name="task-delete"),
]
