from django.urls import path
from . import views
from .views import HomeListView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('geodata/', views.get_map, name='map'),
]
