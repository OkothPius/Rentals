from django.contrib import admin
from .models import Rental, Sale, Category

admin.site.register(Rental)
admin.site.register(Sale)
admin.site.register(Category)
