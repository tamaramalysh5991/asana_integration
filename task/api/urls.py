from django.urls import path

from .views import TaskListAPIView, TaskDetailAPIView

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view()),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view()),
]
