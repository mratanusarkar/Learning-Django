"""View for Gadgets and Brands"""

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Gadget, Brand


class GadgetDetailView(DetailView):
    """Gadget Detail View extending django DetailView and linking html template"""

    model = Gadget
    template_name = "gadgets/gadget_details.html"


class GadgetListView(ListView):
    """Gadget List View extending django ListView and linking html template"""

    model = Gadget
    template_name = "gadgets/gadget_list.html"
