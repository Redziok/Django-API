from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Ratings
from .serializers import RatingAddSerializer, RatingSerializer

@api_view(['GET'])
def getRatings(request):
    ratings = Ratings.objects.all()
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRating(request, pk):
    rating = Ratings.objects.get(id=pk)
    serializer = RatingSerializer(rating, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addRating(request):
    book = request.data['book']
    User = request.data['User']
    serializer = RatingAddSerializer(data=request.data)
    if serializer.is_valid():
        check_exist = Ratings.objects.filter(book=book) and Ratings.objects.filter(User=User).exists()
        if check_exist: 
            return Response({'User already rated this book'},status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
        return Response({'Successfully added Rating to database'},status.HTTP_201_CREATED)
    else:
        return Response({'Failed to add Rating to database'},status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateRating(request, pk):
    rating = Ratings.objects.get(id=pk)
    serializer = RatingSerializer(rating, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Successfully updated Rating'},status.HTTP_201_CREATED)
    else:
        return Response({'Failed to update Rating'},status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteRating(request, pk):
    ratings = Ratings.objects.get(id=pk)
    ratings.delete()
    return Response({'Rating successfully deleted'}, status.HTTP_204_NO_CONTENT)