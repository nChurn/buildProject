from django.urls import path

from floors import views

app_name = "floors"

urlpatterns = [
    path("floors/<int:pk>", views.FloorDetailView.as_view(), name="floor_detail"),
    path("floors/", views.FloorListView.as_view(), name="floor_list"),
]
