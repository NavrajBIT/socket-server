from . import views
from django.urls import include, path

urlpatterns = [
    path("", views.api_check),
]
