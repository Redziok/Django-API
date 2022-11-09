from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Persons
from .serializers import PersonSerializer
from django.http import Http404

@api_view(['GET','POST'])
def getPersons(request):
    if request.method == 'GET':
        persons = Persons.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Successfully added Person to database'}, status.HTTP_201_CREATED)
        else:
            return Response({'Failed to add Person to database'}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def personDetail(request, pk):
    try:
        person = Persons.objects.get(id=pk)
    except Persons.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Successfully updated Person'}, status.HTTP_201_CREATED)
        else:
            return Response({'Failed to update Person'}, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response({'Person successfully deleted'}, status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def personGetContain(request, string):
    persons = Persons.objects.all()
    personContain = request.query_params.get(string)
    if personContain is not None:
        persons = persons.filter(imie=string)
    return persons



# class PersonController(generics.GenericAPIView):
#
#     def get(self, request):
#         persons = Persons.objects.all()
#         serializer = PersonSerializer(persons, many=True)
#         return Response({
#             "person": serializer.data
#         })
#
#     def post(self, request):
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def getObject(self, request, pk):
#         person = Persons.objects.get(id=pk)
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         person = Persons.objects.get(id=pk)
#         serializer = PersonSerializer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'success': True,
#                 'message': 'APIView: updated Person',
#                 "person": serializer.data
#             })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         person = Persons.objects.get(id=pk)
#         person.delete()
#         return Response({
#             'success': True,
#             'message': 'Successfully deleted Persons'
#         })