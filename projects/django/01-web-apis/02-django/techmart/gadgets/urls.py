"""Gadgets URL Configuration"""

from django.urls import path
from .views import GadgetDetailView, GadgetListView
from .views import gadget_list

urlpatterns = [
    path("gadgets/", GadgetListView.as_view(), name="gadget-list"),
    path("gadgets/<int:pk>/", GadgetDetailView.as_view(), name="gadget-details"),

    path("api/gadgets/", gadget_list, name="gadget-list-api"),
]
