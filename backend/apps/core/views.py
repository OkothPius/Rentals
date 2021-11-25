import requests
from django.utils import timezone

from django.shortcuts import render
from django.views import generic
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Rental
from django.views.generic import (
                    ListView,
                    CreateView,
                    UpdateView,
                    DetailView,
                    DeleteView
                    )

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

# @login_required
class HomeListView(LoginRequiredMixin, generic.ListView):
    models = Rental
    template_name = 'core/index.html'
    redirect_field_name = 'home'
    queryset = Rental.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class RentalCreateView(LoginRequiredMixin, CreateView):
    model = Rental
    fields = ['name', 'rent', 'house_detail', 'type', 'location', 'image']

class RentalUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    success_message ='Your Post have been Updated!'
    model = Rental
    fields = ['name', 'rent', 'house_detail', 'type', 'location', 'image']

    # Uses the current user as the author of posts created
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        rental = self.get_object()
        if self.request.user == rental.author:
            return True

class RentalDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    success_message ='Your Post have been Deleted!'
    model = Rental
    success_url = '/'

    def test_func(self):
        rental = self.get_object()
        if self.request.user == rental.author:
            return True
