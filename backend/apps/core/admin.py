from django.contrib import admin
from .models import Rental, Sale, Category


class RentalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                         {'fields': ['pub_date', 'name']}),
        ('House Description Details' , {'fields': ['house_detail', 'rent', 'location', 'image'], 'classes': ['collapse']}),
    ]

    list_display = ('name', 'pub_date')

    list_filter = ['pub_date']

    search_fields = ['name']

admin.site.register(Rental, RentalAdmin)
admin.site.register(Sale)
admin.site.register(Category)
