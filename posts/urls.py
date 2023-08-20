from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view())
    path('posts/<int:post_id>/report/', views.ReportCreate.as_view()),
]