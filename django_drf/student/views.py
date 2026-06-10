from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import StudentSerializers
from .models import Student
class StudentListview(APIView):
    def get(self,request):
        student=Student.objects.all()
        serializer=StudentSerializers(student,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)        
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        student=Student.objects.get(pk=pk)    
        serializer=StudentSerializers(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)        
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        student=Student.objects.get(pk=pk)
        student.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT)
    
    
