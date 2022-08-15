from django.urls import path

from sections import views


app_name = "sections"

urlpatterns = [
    path("sections/", views.SectionListView.as_view(), name="section_list"),
    path("sections/<int:pk>", views.SectionDetailView.as_view(), name="section_detail"),
]
