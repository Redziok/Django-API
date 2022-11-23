from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from base.models import Author
from .serializers import AuthorSerializer


# AUTHORS REQUESTS
@api_view(['GET'])
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_author(request, pk):
    author = get_object_or_404(Author, id=pk)
    serializer = AuthorSerializer(author, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Successfully added Author to database'}, status.HTTP_201_CREATED)
    else:
        return Response({'Failed to add Author to database'}, status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_author(request, pk):
    author = get_object_or_404(Author, id=pk)
    serializer = AuthorSerializer(author, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Successfully updated Author'}, status.HTTP_201_CREATED)
    else:
        return Response({'Failed to update Author'}, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, permissions.IsAdminUser])
def delete_author(request, pk):
    authors = get_object_or_404(Author, id=pk)
    authors.delete()
    return Response({'Author successfully deleted'}, status.HTTP_204_NO_CONTENT)
