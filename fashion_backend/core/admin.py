from django.contrib import admin
# from .models import Brand
from . import models

# Register your models here.
admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.Product)


