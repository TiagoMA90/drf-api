from django.urls import path
from reports import views

urlpatterns = [
    path('report/', views.ReportList.as_view()),
    path('report/<int:pk>/', views.ReportDetail.as_view()),
    path('posts/<int:post_pk>/reports/', views.ReportList.as_view()),
    path('posts/<int:post_pk>/reports/<int:pk>/', views.ReportDetail.as_view()),
]
