from base.models import Persons
from persons.serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

person = Persons(name='Adam', miesiac_dodania=1)
person.save()

serializer = PersonSerializer(person)
serializer.data

content = JSONRenderer().render(serializer.data)

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = PersonSerializer(data=data)
deserializer.is_valid()

deserializer.errors

deserializer.fields

deserializer.validated_data
deserializer.save()

deserializer.data