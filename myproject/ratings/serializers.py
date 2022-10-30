from rest_framework import serializers
from base.models import Ratings

# User Serializer
class RatingSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    User = serializers.StringRelatedField()
    class Meta:
        model = Ratings
        fields = '__all__'

class RatingAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'