from rest_framework import serializers
from base.models import Persons, Druzyna

class PersonSerializer(serializers.Serializer):
    class Meta:
        model = Persons
        fields = ['imie', 'nazwisko', 'miesiac_urodzenia', 'Drużyna']

# Register Serializer
class DruzynaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Druzyna
        fields = '__all__'

# class PersonSerializer(serializers.Serializer):
#     imie = serializers.CharField(required=True)
#     miesiac_urodzenia = serializers.ChoiceField(choices=Persons.miesiace, default=Persons.miesiace[0][0])
#     Drużyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())
#
# class DruzynaSerializer(serializers.Serializer):
#     nazwa = serializers.CharField(required=True)
#     kraj = serializers.CharField(required=True)