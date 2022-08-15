from django.urls import path

from pages import views


app_name = "pages"

urlpatterns = [
    path("pages", views.PageListView.as_view(), name="page_list"),
    path("pages/<str:slug>", views.PageDetailView.as_view(), name="page_detail"),
]
