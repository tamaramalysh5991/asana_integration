from django.urls import path

from .views import ProjectListAPIView, ProjectDetailAPIView

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view()),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view()),
]
