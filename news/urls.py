from django.urls import path

from news import views

app_name = "news"

urlpatterns = [
    path("news/", views.PublicationListView.as_view(), name="publication_list"),
    path(
        "news/<str:slug>",
        views.PublicationDetailView.as_view(),
        name="publication_detail",
    ),
]
