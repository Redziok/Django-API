from base.models import Persons
from persons.serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

person = Persons(imie='Adam', miesiac_urodzenia=1)
person.save()

serializer = PersonSerializer(person)
serializer.data

content = JSONRenderer().render(serializer.data)

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = PersonSerializer(data=data)
deserializer.is_valid()

deserializer.errors

deserializer.fields
deserializer.validated_data
deserializer.save()

deserializer.data

------------------------------------------------------------
from base.models import Druzyna
from persons.serializers import DruzynaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

druzyna = Druzyna(nazwa='Wilki', kraj='PL')
druzyna.save()

serializer = DruzynaSerializer(druzyna)
serializer.data

content = JSONRenderer().render(serializer.data)

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = DruzynaSerializer(data=data)
deserializer.is_valid()

deserializer.errors

deserializer.fields
deserializer.validated_data
deserializer.save()

deserializer.data