from django.urls import path
from . import views
from .views import (
            RentalListView,
            SaleListView,
            RentalCreateView,
            RentalUpdateView,
            RentalDeleteView,
            SaleCreateView,
            SaleUpdateView,
            SaleDeleteView,
            SearchView,
            PdfView,
            )

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('map/', views.default_maps, name='map'),
    path('', RentalListView.as_view(), name='rental'),
    path('rental/new/', RentalCreateView.as_view(), name='rental-create'),
    path('rental/<int:pk>/update/', RentalUpdateView.as_view(), name='rental-update'),
    path('rental/<int:pk>/delete/', RentalDeleteView.as_view(), name='rental-delete'),
    path('sale/new/', SaleCreateView.as_view(), name='sale-create'),
    path('sale/', SaleListView.as_view(), name='sale'),
    path('sale/<int:pk>/update/', SaleUpdateView.as_view(), name='sale-update'),
    path('sale/<int:pk>/delete/', SaleDeleteView.as_view(), name='sale-delete'),
    path('search/', SearchView.as_view(), name='search'),
    path('download/', PdfView.as_view(), name='download'),
]
