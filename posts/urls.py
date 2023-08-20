from django.urls import path
from django.urls import include
from posts import views
from reports import urls as report_urls

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/<int:pk>/report/', include(report_urls)),
]