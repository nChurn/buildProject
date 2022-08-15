from django.urls import path
from buildings import views


app_name = "buildings"

urlpatterns = [
    path("", views.BuildingListView.as_view(), name="building_list"),
    path("<int:pk>", views.BuildingListView.as_view(), name="building_list"),
]
