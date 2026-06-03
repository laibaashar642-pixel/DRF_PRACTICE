from django.shortcuts import render
from rest_framework.views import APIView, Http404
from rest_framework.views import Response
from rest_framework.views import status
from rest_framework import generics

from .models import Student
from .serializers import BookSerializer, StudentSerializer
# Create your views here.
#Generic View
class StudentDetailView(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
class StudentListView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        serializer=StudentSerializer(Student,data=request.data):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        student=self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#Drf mai teen trah ki views hoti hai API VIEW ,Generic View,Viewset sb sai zyada complex or jis mai sb sai zyada code likha jata hai wo api view aur jis may short built in terms likhi jati hai but  code bhi likha jata hai less aur last is view set jis mai code likha hi nai jata simple routers sai automatic lia jata hai
#APIViewGET, POST, PUT, DELETE — har method khud likhni hai. Zyada code but full control.GenericViewSirf queryset aur serializer_class batao — baaki DRF karta hai. Bohot kam code.
""" Kb konsa use karein?
APIView
Complex logic — multiple models, custom authentication, non-standard responses
GenericView
Standard CRUD — list, create, retrieve, update, delete
ViewSet
Poora REST API quickly banana ho — Topic 4 mein cover hoga """
#Get Api View for gett,post,put,delete
#in generic form the code is
# List + Create — GET aur POST dono!
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Retrieve + Update + Delete — GET, PUT, DELETE!
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer