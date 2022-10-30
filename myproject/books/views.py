from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Books
from .serializers import BookAddSerializer, BookSerializer

def to_representation(self, instance):
    rep = super(BookSerializer, self).to_representation(instance)
    rep['author'] = instance.author
    return rep
    
@api_view(['GET'])
def getBooks(request):
    books = Books.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBook(request, pk):
    book = Books.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addBook(request):
    serializer = BookAddSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Successfully added Book to database'},status.HTTP_201_CREATED)
    else:
        return Response({'Failed to add Book to database'},status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateBook(request, pk):
    book = Books.objects.get(id=pk)
    serializer = BookAddSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Successfully updated Book'},status.HTTP_201_CREATED)
    else:
        return Response({'Failed to update Book'},status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteBook(request, pk):
    books = Books.objects.get(id=pk)
    books.delete()
    return Response({'Book successfully deleted'}, status.HTTP_204_NO_CONTENT)