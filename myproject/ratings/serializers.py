from rest_framework import serializers
from base.models import Ratings

# User Serializer
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'