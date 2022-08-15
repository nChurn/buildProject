from django.urls import path

from main_pages import views

app_name = "main_pages"


urlpatterns = [
    path("company", views.CompanyView.as_view(), name="company"),
    path("investors", views.InvestorView.as_view(), name="investor"),
]
