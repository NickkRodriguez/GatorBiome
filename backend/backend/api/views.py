import pandas as pd
import os
from django.shortcuts import render
from rest_framework import viewsets, status
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import ModelMetrics, MLModel, Dataset
from .serializers import DatasetSerializer, MLModelSerializer, ModelMetricsSerializer
from rest_framework.parsers import MultiPartParser, FormParser
import subprocess
import base64
import json
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

class FeatureEngineeringResultsView(APIView):
    def get(self, request):
        dataset_name = request.query_params.get('dataset_name')

        if dataset_name:
            csv_path = os.path.join(settings.RESULTS_DIR, f'feature_eng_results_{dataset_name}.csv')
            print(f"CSV Path: {csv_path}")
            
            if os.path.exists(csv_path):
                try:
                    df = pd.read_csv(csv_path)
                    result_data = df.to_dict(orient='records')

                    charts_path = os.path.join(settings.RESULTS_DIR, 'visuals', dataset_name)
                    chart_images = {
                        "accuracy": os.path.join(charts_path, f"{dataset_name}_heatmap_accuracy.png"),
                        "auc": os.path.join(charts_path, f"{dataset_name}_heatmap_auc.png"),
                        "f1": os.path.join(charts_path, f"{dataset_name}_heatmap_f1.png"),
                        "precision": os.path.join(charts_path, f"{dataset_name}_heatmap_precision.png"),
                    }

                    return Response({
                        "data": result_data,
                        "charts": chart_images
                    }, status=status.HTTP_200_OK)

                except Exception as e:
                    return Response(
                        {"error": f"Error reading the file: {str(e)}"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
            else:
                return Response(
                    {"error": f"Feature engineering results for dataset '{dataset_name}' not found at {csv_path}"},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response({"error": "Dataset name is required"}, status=status.HTTP_400_BAD_REQUEST)
        
class DatasetView(APIView):
    def get(self, request):
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

        if ModelMetrics.objects.filter(
                model_id=request.data['model'],
                dataset_id=request.data['dataset']
        ).exists():
            return Response(
                {"error": "Metrics for this model-dataset combination already exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ModelMetricsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        
        if not file_obj:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
        if not file_obj.name.endswith('.csv'):
            return Response({'error': 'File must be a CSV'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            df = pd.read_csv(file_obj)
            
            return Response({
                'message': 'File uploaded successfully',
                'rows': len(df),
                'columns': list(df.columns)
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DatasetUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        train_file = request.FILES.get('train')
        test_file = request.FILES.get('test')
        
        if not train_file or not test_file:
            return Response({'error': 'Both train and test CSV files are required'}, 
                           status=status.HTTP_400_BAD_REQUEST)
            
        if not train_file.name.endswith('.csv') or not test_file.name.endswith('.csv'):
            return Response({'error': 'Files must be CSV format'}, 
                           status=status.HTTP_400_BAD_REQUEST)
            
        try:
            project_root = os.path.join(settings.BASE_DIR, '..')
            data_dir = os.path.join(project_root, 'data')
            os.makedirs(data_dir, exist_ok=True)
            
            train_path = os.path.join(data_dir, 'train.csv')
            test_path = os.path.join(data_dir, 'test.csv')
            
            with open(train_path, 'wb+') as destination:
                for chunk in train_file.chunks():
                    destination.write(chunk)
                    
            with open(test_path, 'wb+') as destination:
                for chunk in test_file.chunks():
                    destination.write(chunk)
            
            scripts = [
                f"cd {project_root} && jupyter nbconvert --to notebook --execute training_pipeline.ipynb",
                f"cd {project_root} && jupyter nbconvert --to notebook --execute feature_engineering.ipynb",
                f"cd {project_root} && jupyter nbconvert --to notebook --execute ensemble_modeling.ipynb"
            ]
            
            results = []
            for script in scripts:
                process = subprocess.run(script, shell=True, capture_output=True, text=True)
                results.append({
                    'command': script,
                    'return_code': process.returncode,
                    'stdout': process.stdout,
                    'stderr': process.stderr
                })
            
            return Response({
                'message': 'Files uploaded and processing pipeline completed',
                'pipeline_results': results
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PipelineResultsView(APIView):
    def get(self, request):
        try:
            file_name = request.query_params.get('name', '')
            file_name = file_name.strip("'\"")
            
            project_root = os.path.join(settings.BASE_DIR, '..', '..')
            summaries_dir = os.path.join(project_root, 'results', 'summaries')
            visuals_dir = os.path.join(project_root, 'results', 'visuals', 'ensemble')
            
            print(f"Project root: {project_root}")
            print(f"Summaries dir: {summaries_dir}")
            print(f"Visuals dir: {visuals_dir}")
            print(f"Requested file: {file_name}")
            
            if not file_name:
                results_file = os.path.join(summaries_dir, 'ensemble_metrics.json')
                csv_results_file = os.path.join(summaries_dir, 'ensemble_results.csv')
                
                print(f"Looking for default results file: {results_file}")
                
                if not os.path.exists(results_file):
                    available_files = []
                    if os.path.exists(summaries_dir):
                        available_files = os.listdir(summaries_dir)
                    
                    return Response({
                        'error': 'Results not available yet',
                        'looked_for': results_file,
                        'available_files': available_files
                    }, status=status.HTTP_404_NOT_FOUND)
                
                with open(results_file, 'r') as f:
                    results_data = json.load(f)
                
                best_method = None
                best_auc = 0
                
                for model, metrics in results_data.items():
                    if metrics.get('AUC', 0) > best_auc:
                        best_auc = metrics.get('AUC', 0)
                        best_method = model
                
                image_files = {}
                if os.path.exists(visuals_dir):
                    for file in os.listdir(visuals_dir):
                        if file.endswith('.png'):
                            img_path = os.path.join(visuals_dir, file)
                            with open(img_path, 'rb') as img_file:
                                encoded_img = base64.b64encode(img_file.read()).decode('utf-8')
                                image_files[file] = f"data:image/png;base64,{encoded_img}"
                
                response = {
                    'best_method': best_method,
                    'metrics': results_data.get(best_method, {}),
                    'all_results': results_data,
                    'file_paths': {
                        'json': results_file,
                        'csv': csv_results_file if os.path.exists(csv_results_file) else None
                    },
                    'visualization_data': image_files
                }
                
                return Response(response, status=status.HTTP_200_OK)
            
            else:
                if file_name.endswith('.json'):
                    file_path = os.path.join(summaries_dir, file_name)
                    print(f"Looking for JSON file: {file_path}")
                    
                    if not os.path.exists(file_path):
                        available_files = []
                        if os.path.exists(summaries_dir):
                            available_files = os.listdir(summaries_dir)
                        
                        return Response({
                            'error': f'File {file_name} not found',
                            'looked_for': file_path,
                            'available_files': available_files
                        }, status=status.HTTP_404_NOT_FOUND)
                    
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                    return Response(data, status=status.HTTP_200_OK)
                
                elif file_name.endswith('.csv'):
                    file_path = os.path.join(summaries_dir, file_name)
                    print(f"Looking for CSV file: {file_path}")
                    
                    if not os.path.exists(file_path):
                        available_files = []
                        if os.path.exists(summaries_dir):
                            available_files = os.listdir(summaries_dir)
                        
                        return Response({
                            'error': f'File {file_name} not found',
                            'looked_for': file_path,
                            'available_files': available_files
                        }, status=status.HTTP_404_NOT_FOUND)
                    
                    df = pd.read_csv(file_path)
                    return Response(df.to_dict(orient='records'), status=status.HTTP_200_OK)
                
                elif file_name.endswith(('.png', '.jpg', '.jpeg')):
                    file_path = os.path.join(visuals_dir, file_name)
                    print(f"Looking for image file: {file_path}")
                    
                    if not os.path.exists(file_path):
                        available_files = []
                        if os.path.exists(visuals_dir):
                            available_files = os.listdir(visuals_dir)
                        
                        return Response({
                            'error': f'File {file_name} not found',
                            'looked_for': file_path,
                            'available_files': available_files
                        }, status=status.HTTP_404_NOT_FOUND)
                    
                    with open(file_path, 'rb') as img_file:
                        encoded_img = base64.b64encode(img_file.read()).decode('utf-8')
                    
                    content_type = 'image/png' if file_name.endswith('.png') else 'image/jpeg'
                    
                    return Response({
                        'image': f"data:{content_type};base64,{encoded_img}",
                        'name': file_name
                    }, status=status.HTTP_200_OK)
                
                else:
                    available_files = {'summaries': [], 'visuals': []}
                    
                    if os.path.exists(summaries_dir):
                        available_files['summaries'] = os.listdir(summaries_dir)
                    
                    if os.path.exists(visuals_dir):
                        available_files['visuals'] = os.listdir(visuals_dir)
                    
                    return Response({
                        'error': 'Unsupported file type or file not specified correctly',
                        'requested': file_name,
                        'available_files': available_files,
                        'hint': 'Try using one of the available files with ?name=filename.ext'
                    }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            import traceback
            traceback_str = traceback.format_exc()
            return Response({
                'error': str(e),
                'traceback': traceback_str
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
