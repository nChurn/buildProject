from django.urls import path

from layouts import views

app_name = "layouts"


urlpatterns = [
    path("layouts", views.LayoutListView.as_view(), name="layout_list"),
    path("layouts/<int:pk>", views.LayoutDetailView.as_view(), name="layout_detail"),
]
