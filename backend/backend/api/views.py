from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Wine, ModelMetrics, MLModel, Dataset
from .serializers import WineSerializer, DatasetSerializer, MLModelSerializer, ModelMetricsSerializer


class WineViewSet(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer

class DatasetView(APIView):
    def get(self, request):
        # Option 1: Get a specific dataset by name
        dataset_name = request.query_params.get('name')
        if dataset_name:
            try:
                dataset = Dataset.objects.get(name=dataset_name)
                serializer = DatasetSerializer(dataset)
                return Response(serializer.data)
            except Dataset.DoesNotExist:
                return Response(
                    {"error": f"Dataset with name '{dataset_name}' not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        # Option 2: Get all datasets
        else:
            datasets = Dataset.objects.all()
            serializer = DatasetSerializer(datasets, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = DatasetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MLModelView(APIView):
    def get(self, request):
        # Option 1: Get a specific dataset by name
        mlmodel_name = request.query_params.get('name')
        if mlmodel_name:
            try:
                mlmodel = MLModel.objects.get(name=mlmodel_name)
                serializer = MLModelSerializer(mlmodel)
                return Response(serializer.data)
            except MLModel.DoesNotExist:
                return Response(
                    {"error": f"MLModel with name '{mlmodel_name}' not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        # Option 2: Get all datasets
        else:
            mlmodels = MLModel.objects.all()
            serializer = MLModelSerializer(mlmodels, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = MLModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModelMetricsView(APIView):
    def get(self, request):
        """
        Get model metrics filtered by model name and dataset name
        Example: /api/model-metrics/?model_name=RandomForest&dataset_name=Wine
        """
        model_name = request.query_params.get('model_name')
        dataset_name = request.query_params.get('dataset_name')

        queryset = ModelMetrics.objects.all()

        if model_name:
            queryset = queryset.filter(model__name=model_name)

        if dataset_name:
            queryset = queryset.filter(dataset__name=dataset_name)

        if model_name and dataset_name and not queryset.exists():
            return Response(
                {"message": f"No metrics found for model '{model_name}' on dataset '{dataset_name}'"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ModelMetricsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        if 'model' not in request.data or 'dataset' not in request.data:
            return Response(
                {"error": "Both 'model' and 'dataset' are required fields"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            MLModel.objects.get(id=request.data['model'])
        except MLModel.DoesNotExist:
            return Response(
                {"error": f"Model with ID {request.data['model']} does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            Dataset.objects.get(id=request.data['dataset'])
        except Dataset.DoesNotExist:
            return Response(
                {"error": f"Dataset with ID {request.data['dataset']} does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if metrics for this model-dataset pair already exist
        if ModelMetrics.objects.filter(
                model_id=request.data['model'],
                dataset_id=request.data['dataset']
        ).exists():
            return Response(
                {"error": "Metrics for this model-dataset combination already exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validate and create the metrics
        serializer = ModelMetricsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
