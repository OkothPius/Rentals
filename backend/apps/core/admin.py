from django.contrib import admin
from .models import Rental, Sale, Category, Message


admin.site.register(Rental)
admin.site.register(Message)
admin.site.register(Sale)
admin.site.register(Category)
