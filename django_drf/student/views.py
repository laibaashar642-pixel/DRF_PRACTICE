from.models import Student
from.serializer import StudentSerializers
from rest_framework.status import Status
from rest_framework import Response
from rest_framework import APIView
class StudentListView():
    def get(self,request):
        student=Student.objects.all()
        serializer=StudentSerializers(Student,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            return serializer.save()
        return Response(serializer.data,status=Status.HTTP_201_CREATED)
    
        return Response(serializer.errors,status=Status.HTTP_400_BAD_REQUEST)