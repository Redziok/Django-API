from rest_framework import serializers
from base.models import Person, Team

class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=Person.miesiace)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Person
        fields = ['imie', 'nazwisko', 'miesiac_urodzenia', 'Drużyna', 'owner']

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_urodzenia = validated_data.get('miesiac_urodzenia', instance.miesiac_urodzenia)
        instance.Drużyna = validated_data.get('Drużyna', instance.Drużyna)
        instance.save()
        return instance


# class PersonSerializer(serializers.Serializer):
#     imie = serializers.CharField(required=True)
#     miesiac_urodzenia = serializers.ChoiceField(choices=Person.miesiace, default=Person.miesiace[0][0])
#     Drużyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())
