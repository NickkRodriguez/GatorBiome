from django.urls import path

from .models import MLModel, ModelMetrics
from .views import (DatasetView, ModelMetricsView, MLModelView, 
                   FeatureEngineeringResultsView, FileUploadView, 
                   DatasetUploadView, PipelineResultsView)

urlpatterns = [
    path('datasets/', DatasetView.as_view(), name='dataset-list'),
    path('models/', MLModelView.as_view(), name='model-list'),
    path('metrics/', ModelMetricsView.as_view(), name='metrics-list'),
    path('feature-engineering/', FeatureEngineeringResultsView.as_view(), name='feature-engineering-results'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('dataset-upload/', DatasetUploadView.as_view(), name='dataset-upload'),
    path('results/', PipelineResultsView.as_view(), name='pipeline-results'),
]