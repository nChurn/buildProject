from django.urls import path

from data import views


app_name = "data"


urlpatterns = [
    path("organization", views.OrganizationView.as_view(), name="organization"),
    path("banks", views.BankListView.as_view(), name="bank_list"),
]
