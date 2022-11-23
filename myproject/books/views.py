from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from base.models import Book
from .serializers import BookAddSerializer, BookSerializer


def to_representation(self, instance):
    rep = super(BookSerializer, self).to_representation(instance)
    rep['author'] = instance.author
    return rep


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_book(request):
    serializer = BookAddSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Successfully added Book to database'}, status.HTTP_201_CREATED)
    else:
        return Response({'Failed to add Book to database'}, status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    serializer = BookAddSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Successfully updated Book'}, status.HTTP_201_CREATED)
    else:
        return Response({'Failed to update Book'}, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, permissions.IsAdminUser])
def delete_book(request, pk):
    books = get_object_or_404(Book, id=pk)
    books.delete()
    return Response({'Book successfully deleted'}, status.HTTP_204_NO_CONTENT)
