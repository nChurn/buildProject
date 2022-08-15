from django.urls import path

from forms import views


app_name = "forms"

urlpatterns = [
    path("backcall", views.BackCallCreateView.as_view(), name="backcall_create")
]
