from django.urls import path
from walls import views

urlpatterns = [
    path('walls/', views.WallPostList.as_view()),
    path('walls/<int:pk>/', views.WallPostDetail.as_view())
]
