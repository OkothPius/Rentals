from django.urls import path
from . import views
from .views import HomeListView, RentalCreateView,RentalUpdateView, RentalDeleteView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('geodata/', views.get_map, name='map'),
    path('rental/<int:pk>/update/', RentalUpdateView.as_view(), name='rental-update'),
    path('rental/<int:pk>/delete/', RentalDeleteView.as_view(), name='rental-delete'),
]
