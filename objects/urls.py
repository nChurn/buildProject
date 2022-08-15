from django.urls import path

from objects import views

app_name = "objects"

urlpatterns = [
    path("objects/", views.ObjectListView.as_view(), name="object_list"),
    path("objects/<int:pk>", views.ObjectDetailView.as_view(), name="object_detail"),
]
