from django.urls import path
from .views import ReportCreate

urlpatterns = [
    path('posts/<int:post_id>/report/', ReportCreate.as_view()),
]
