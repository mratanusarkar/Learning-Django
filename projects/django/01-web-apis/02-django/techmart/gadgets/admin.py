"""register the models to django admin"""

from django.contrib import admin

from .models import Gadget, Brand

admin.site.register(Gadget)
admin.site.register(Brand)
