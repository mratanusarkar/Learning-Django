"""Gadgets URL Configuration"""

from django.urls import path
from .views import GadgetDetailView, GadgetListView

urlpatterns = [
    path("", GadgetListView.as_view(), name="gadget-list"),
    path("gadgets/<int:pk>/", GadgetDetailView.as_view(), name="gadget-details")
]
