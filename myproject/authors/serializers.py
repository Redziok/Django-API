from rest_framework import serializers
from base.models import Authors

# User Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'