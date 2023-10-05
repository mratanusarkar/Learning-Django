"""View for Gadgets and Brands"""

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse

from .models import Gadget, Brand


# generic class based views

class GadgetDetailView(DetailView):
    """Gadget Detail View extending django DetailView and linking html template"""

    model = Gadget
    template_name = "gadgets/gadget_details.html"


class GadgetListView(ListView):
    """Gadget List View extending django ListView and linking html template"""

    model = Gadget
    template_name = "gadgets/gadget_list.html"


# json response views

def gadget_list(request):
    gadgets = Gadget.objects.all()  # we can also get a slice. say [:30]
    data = {
        "gadgets": list(gadgets.values("pk", "name"))
    }
    response = JsonResponse(data)
    return response