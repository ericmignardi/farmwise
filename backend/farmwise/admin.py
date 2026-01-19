from django.contrib import admin
from .models import Farm, Crop, Asset, WealthRecord

# Register your models here.

admin.site.register(Farm)
admin.site.register(Crop)
admin.site.register(Asset)
admin.site.register(WealthRecord)
