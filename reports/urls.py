from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:post_id>/report/', views.ReportCreate.as_view()),
    path('posts/<int:post_id>/reports/', views.ReportList.as_view()),
    path('reports/<int:pk>/', views.ReportDetail.as_view()),
]