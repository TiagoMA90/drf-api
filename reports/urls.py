from django.urls import path
from reports import views

urlpatterns = [
    path('reports/', views.ReportList.as_view()),
]