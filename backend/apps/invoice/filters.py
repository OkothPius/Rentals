import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class InvoiceFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_posted", lookup_expr='gte')
    # end_date = DateFilter(field_name="date_posted", lookup_expr='lte')
    tenant = CharFilter(field_name='tenant', lookup_expr='icontains')
    class Meta:
        model = Invoice
        fields = ['tenant', 'date', 'status']
        # exclude = ['date_posted']
