import requests
from django.utils import timezone

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from mapbox import Directions
from django.http import HttpResponse



from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Rental, Sale, Message
from .render import Render
from django.views.generic import (
                    ListView,
                    CreateView,
                    UpdateView,
                    DetailView,
                    DeleteView
                    )
import pdfkit

def home(request):
    return render(request, 'core/home.html')

#Tenant View
def home_tenant(request):
    # tenant = User.objects.filter(is_tenant=True)
    rentals = Rental.objects.all()
    sales = Sale.objects.all()

    context = {'rentals':rentals, 'sales':sales}
    return render(request, 'core/tenant_home.html', context)



class RentalListView(generic.ListView):
    models = Rental
    template_name = 'core/index.html'
    redirect_field_name = 'home'
    queryset = Rental.objects.all()
    context_object_name = 'rentals'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class RentalCreateView(CreateView):
    """
    Create View for Sale Model.
    """
    model = Rental
    fields = ['name', 'rent', 'house_detail', 'type', 'location', 'image']

    #Uses the current user as the author of posts created
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RentalUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
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

class RentalDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    success_message ='Your Post have been Deleted!'
    model = Rental
    success_url = '/'

    def test_func(self):
        rental = self.get_object()
        if self.request.user == rental.author:
            return True

class SaleListView(generic.ListView):
    models = Sale
    template_name = 'core/sale.html'
    redirect_field_name = 'home'
    queryset = Sale.objects.all()
    context_object_name = 'sales'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class SaleCreateView(CreateView):
    """
    Create View for Sale Model.
    """
    model = Sale
    fields = ['name', 'price', 'house_detail', 'type', 'location', 'image']

    #Uses the current user as the author of posts created
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MessageCreateView(CreateView):
    model = Message
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class SaleUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    success_message ='Your Post have been Updated!'
    model = Sale
    fields = ['name', 'price', 'house_detail', 'type', 'location', 'image']

    # Uses the current user as the author of posts created
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        rental = self.get_object()
        if self.request.user == rental.author:
            return True

class SaleDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    success_message ='Your Post have been Deleted!'
    model = Sale
    success_url = '/'

    def test_func(self):
        rental = self.get_object()
        if self.request.user == rental.author:
            return True

#Search view
class SearchView(generic.TemplateView):
    template_name = 'core/search.html'
    models = Rental

    def get_queryset(self):
        return Rental.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get('keyword')
        results = Rental.objects.filter(
            Q(name__icontains=kw) | Q(location__icontains=kw) | Q(rent__icontains=kw))
        print('results')
        context['results'] = results
        return context

# Generating PDF file for each specific listing
class PdfView(generic.TemplateView):

    def get(self, request):
        rental = Rental.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'rental': rental,
            'request': request
        }
        return Render.render('core/pdf.html', params)

def default_maps(request):
	# TODO: move Token to settings.py file
	mapbox_access_token = 'pk.eyJ1Ijoib3J1a28iLCJhIjoiY2t3ajBjZmthMHhuYzJwbWRuOGtucmoxMSJ9.yroz5quTvncPl238zBe_tA'

	return render(request, 'core/map.html', {'mapbox_access_token':mapbox_access_token})

#Rental Download
def view_PDF(request):
    rental = Rental.objects.all()

    context = {
        "company": {
            "name": "Arexa Rental Services",
            "address" :"67542 Westlands, Dunham Towers, Kenya",
            "phone": "(254) XXX XXXX",
            "email": "contact@arexa.com",
        },
        'rental':rental,

    }
    return render(request, 'core/pdf_template.html', context)

def generate_PDF(request):
    # Use False instead of output path to save pdf to a variable
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('rental-detail')), False)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rental.pdf"'

    return response

#Sale Download
def sale_PDF(request):
    sale = Sale.objects.all()

    context = {
        "company": {
            "name": "Arexa Rental Services",
            "address" :"67542 Westlands, Dunham Towers, Kenya",
            "phone": "(254) XXX XXXX",
            "email": "contact@arexa.com",
        },
        'sale':sale,

    }
    return render(request, 'core/sale_pdf_template.html', context)

def sale_generate_PDF(request):
    # Use False instead of output path to save pdf to a variable
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('sale-detail')), False)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sale.pdf"'

    return response
