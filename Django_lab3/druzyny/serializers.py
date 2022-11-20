from rest_framework import serializers
from base.models import Druzyna

class DruzynaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Druzyna
        fields = '__all__'
        allow_null = ['kraj']

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance


# class DruzynaSerializer(serializers.Serializer):
#     nazwa = serializers.CharField(required=True)
#     kraj = serializers.CharField(required=True)