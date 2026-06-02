#python sai data ata hai objects ki forrm mai jb kai serializer data ko json format mai convert kr deta hai taki data ko easily transfer kiya ja sake between different systems. Serializer data ko validate bhi karta hai aur ensure karta hai ki data sahi format mai ho. Iske alawa serializer nested relationships ko bhi handle kar sakta hai, jisse complex data structures ko bhi easily serialize kiya ja sakta hai.Serialization = Python → JSON    Deserialization = JSON → Python
# Basic Serializer mein har field manually likhni padti thi. ModelSerializer automatically model se fields le leta hai!

#Model Serializer
from rest_framework import serializers
from . models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['username','email','course','marks']
#manually serilizer without models
class BookSerializer(serializers.Serializer):
    id    = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    price  = serializers.DecimalField(max_digits=6, decimal_places=2)
    # Har field manually define karni padti hai. Yeh tedious hai — isliye ModelSerializer aaya!
    #to use serilizer in view
"""  book = Book.objects.get(id=1)
serializer = BookSerializer(book)
print(serializer.data)
# Output: {'id': 1, 'title': 'Python Basics', 'author': 'Mark'} """
#to uuse fields
""" fields options — kya include karo
# Option 1 — saari fields
fields = '__all__'

# Option 2 — specific fields hi
fields = ['id', 'title', 'author']

# Option 3 — kuch fields exclude karo
exclude = ['price']  # price nahi chahiye """
""" read_only fields
fields = '__all__'
read_only_fields = ['id']
id sirf read ke liye — user change nahi kar sakta """
""" many=True — list
books = Book.objects.all()
s = BookSerializer(
  books, many=True
)
Multiple objects serialize karne ke liye many=True """
#Nested Serializer if there are multiple models
""" class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()   # nested!
    class Meta:
        model  = Book
        fields = ['id', 'title', 'author'] """
""" 

Validation kya hota hai?
Socho tum ek form fill karo jisme price daalni hai. Agar koi -500 daale — yeh galat hai! Validation yeh check karta hai ke data sahi hai ya nahi save karne se pehle. """
