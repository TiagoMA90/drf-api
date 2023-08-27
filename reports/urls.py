from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.ReportList.as_view()),
    path('reports/<int:pk>/', views.ReportDetail.as_view()),
]
