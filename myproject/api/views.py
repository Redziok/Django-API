from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Authors
from .serializers import AuthorsSerializer

@api_view(['GET'])
def getAuthors(request):
    authors = Authors.objects.all()
    serializer = AuthorsSerializer(authors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAuthor(request, pk):
    author = Authors.objects.get(id=pk)
    serializer = AuthorsSerializer(author, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addAuthor(request):
    serializer = AuthorsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Successfully added Author to database'},status.HTTP_201_CREATED)
    else:
        return Response({'Failed to add Author to database'},status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateAuthor(request, pk):
    author = Authors.objects.get(id=pk)
    serializer = AuthorsSerializer(instance=author, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Successfully updated Author'},status.HTTP_201_CREATED)
    else:
        return Response({'Failed to update Author'},status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteAuthor(request, pk):
    authors = Authors.objects.get(id=pk)
    authors.delete()
    return Response({'Author successfully deleted'}, status.HTTP_204_NO_CONTENT)
