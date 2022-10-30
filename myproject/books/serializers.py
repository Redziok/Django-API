from rest_framework import serializers
from base.models import Books

# User Serializer
class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Books
        fields = '__all__'

class BookAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'