from rest_framework import serializers
from base.models import Book

# User Serializer
class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = '__all__'

class BookAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'