from .models import Student
from rest_framework import Serializers
class StudentSerializers(serializer.Serializers):
    class Meta:
        model=Student
        fields='__all__'