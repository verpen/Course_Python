from django.contrib import admin

from .models import Part
from .models import Rating

admin.site.register(Part)
admin.site.register(Rating)