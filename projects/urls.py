from django.urls import path

from projects import views

app_name = "projects"

urlpatterns = [
    path("cities", views.CityListView.as_view(), name="city_list"),
    path("projects/<int:pk>", views.ProjectDetailView.as_view(), name="project_detail"),
    path("projects/", views.ProjectListView.as_view(), name="project_list"),
]
