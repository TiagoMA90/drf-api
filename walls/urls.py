from django.urls import path
from walls import views


urlpatterns = [
    path('walls/', views.WallList.as_view()),
    path('walls/<int:pk>/', views.WallDetail.as_view()),
    path('profiles/<int:profile_id>/walls/', views.ProfileWalls.as_view()),
]
