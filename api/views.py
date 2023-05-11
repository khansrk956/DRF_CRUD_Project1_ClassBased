from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from . models import Project
from . serializers import ProjectSerializer

class ProjectAPIview(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    


    def post(self, request, *args, **kwargs):
        data = {
            'title':request.data.get('title'),
            'description':request.data.get('description'),
        }
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def delete(self, request, id, *args, **kwargs):
        if Project.objects.filter(id=id).exists():
            project = Project.objects.get(id=id)
            project.delete()
            return Response({'response':'Project Deleted... '}, status=status.HTTP_200_OK)
        else:
            return Response({'res':"Project doesn't exists..."}, status= status.HTTP_400_BAD_REQUEST)
        
    
    def patch(self, request, id, *args, **kwargs):
        if Project.objects.filter(id=id).exists():
            project = Project.objects.get(id=id)
            data = {
                'title':request.data.get('title'),
                'description':request.data.get('description'),
            }
            serializer = ProjectSerializer(instance= project, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        return Response({"res":"Project Doesn't Exists"}, status= status.HTTP_400_BAD_REQUEST)


