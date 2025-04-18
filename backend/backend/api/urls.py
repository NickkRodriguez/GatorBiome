from django.urls import path

from .models import MLModel, ModelMetrics
from .views import WineViewSet, DatasetView, ModelMetricsView, MLModelView, FeatureEngineeringResultsView

urlpatterns = [
    path('wines/', WineViewSet.as_view({'get': 'list'}), name='wine-list'),
    path('datasets/', DatasetView.as_view(), name='dataset-list'),
    path('models/', MLModelView.as_view(), name='model-list'),
    path('metrics/', ModelMetricsView.as_view(), name='metrics-list'),
    path('feature-engineering/', FeatureEngineeringResultsView.as_view(), name='feature-engineering-results'),
]