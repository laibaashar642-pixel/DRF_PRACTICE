from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
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
#Drf mai teen trah ki views hoti hai API VIEW ,Generic View,Viewset sb sai zyada complex or jis mai sb sai zyada code likha jata hai wo api view aur jis may short built in terms likhi jati hai but  code bhi likha jata hai less aur last is view set jis mai code likha hi nai jata simple routers sai automatic lia jata hai
