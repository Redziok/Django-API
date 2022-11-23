from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from base.models import Person

from .permissions import IsOwnerOrReadOnly
from .serializers import PersonSerializer


@api_view(['GET', 'POST'])
def get_person(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Successfully added Person to database'}, status.HTTP_201_CREATED)
        else:
            return Response({'Failed to add Person to database'}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_detail(request, pk):
    try:
        person = Person.objects.get(id=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if person.owner.id == request.user.id:
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        else:
            return Response({"You're not the owner"}, status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
def person_update(request, pk):
    try:
        person = Person.objects.get(id=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Successfully updated Person'}, status.HTTP_201_CREATED)
        else:
            return Response({'Failed to update Person'}, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def person_delete(request, pk):
    try:
        person = Person.objects.get(id=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        person.delete()
        return Response({'Person successfully deleted'}, status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def person_get_contain(request, string):
    persons = Person.objects.all()
    personContain = request.query_params.get(string)
    if personContain is not None:
        persons = persons.filter(imie=string)
    return persons


def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

# class PersonController(generics.GenericAPIView):
#
#     def get(self, request):
#         persons = Person.objects.all()
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
#         person = Person.objects.get(id=pk)
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         person = Person.objects.get(id=pk)
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
#         person = Person.objects.get(id=pk)
#         person.delete()
#         return Response({
#             'success': True,
#             'message': 'Successfully deleted Person'
#         })
