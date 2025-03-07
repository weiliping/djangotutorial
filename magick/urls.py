from django.urls import path
from . import views
from . import persons_api_views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/person/", persons_api_views.PersonView.as_view(), name="persons_list"),
]