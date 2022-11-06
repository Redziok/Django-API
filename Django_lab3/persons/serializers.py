from rest_framework import serializers
from base.models import Persons, Druzyna

class PersonSerializer(serializers.Serializer):
    class Meta:
        model = Persons
        fields = ['imie', 'nazwisko', 'miesiac_urodzenia', 'Drużyna']

    def create(self, validated_data):
        return Persons.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_urodzenia = validated_data.get('miesiac_urodzenia', instance.miesiac_urodzenia)
        instance.Drużyna = validated_data.get('Drużyna', instance.Drużyna)
        instance.save()
        return instance

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

# class PersonSerializer(serializers.Serializer):
#     imie = serializers.CharField(required=True)
#     miesiac_urodzenia = serializers.ChoiceField(choices=Persons.miesiace, default=Persons.miesiace[0][0])
#     Drużyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())
#
# class DruzynaSerializer(serializers.Serializer):
#     nazwa = serializers.CharField(required=True)
#     kraj = serializers.CharField(required=True)