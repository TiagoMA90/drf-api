from django.urls import path
from reports import views

urlpatterns = [
    path('reports/', views.ReportCreate.as_view()),
    path('reports/<int:pk>/', views.ReportDetail.as_view()),
]
