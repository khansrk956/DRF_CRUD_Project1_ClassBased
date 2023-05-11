from django.urls import path
from . views import ProjectAPIview, ProjectDetailAPIView

urlpatterns = [
    path('project',ProjectAPIview.as_view()),
    path('project/<int:id>', ProjectDetailAPIView.as_view()),
]
