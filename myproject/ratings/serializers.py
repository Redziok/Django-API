from rest_framework import serializers
from base.models import Rating

# User Serializer
class RatingSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    User = serializers.StringRelatedField()
    class Meta:
        model = Rating
        fields = '__all__'

class RatingAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'