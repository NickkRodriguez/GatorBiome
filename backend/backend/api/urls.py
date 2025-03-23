from django.urls import path
from .views import WineViewSet

urlpatterns = [
    path('wines/', WineViewSet.as_view({'get': 'list'}), name='wine-list'),
]