import requests
from django.utils import timezone

from django.shortcuts import render
from django.views import generic
from .models import Rental

def get_map(request):
    # ip_address = '41.212.89.70'
    api_key = 'f4c594d1c7f2df990c601cb6cb46c9bf'
    # base_url = 'response/ip_address?access_key=ip_key'
    response = requests.get('http://api.ipstack.com/41.212.89.70?access_key=f4c594d1c7f2df990c601cb6cb46c9bf')
    geodata = response.json()
    return render(request, 'core/map.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'f4c594d1c7f2df990c601cb6cb46c9bf'
    })

class HomeListView(generic.ListView):
    models = Rental
    template_name = 'core/index.html'
    queryset = Rental.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
