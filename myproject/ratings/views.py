from django.db.models import Avg, F
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from base.models import Rating
from .serializers import RatingAddSerializer, RatingSerializer


@api_view(['GET'])
def get_ratings(request):
    ratings = Rating.objects.all()
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_rating(request, pk):
    rating = get_object_or_404(Rating, id=pk)
    serializer = RatingSerializer(rating, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_rating(request):
    book = request.data['book']
    User = request.data['User']
    serializer = RatingAddSerializer(data=request.data)
    if serializer.is_valid():
        if Rating.objects.filter(book=book, User=User).exists():
            return Response({'User already rated this book'}, status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
        return Response({'Successfully added Rating to database'}, status.HTTP_201_CREATED)
    else:
        return Response({'Failed to add Rating to database'}, status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_rating(request, pk):
    rating = get_object_or_404(Rating, id=pk)
    serializer = RatingSerializer(rating, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Successfully updated Rating'}, status.HTTP_201_CREATED)
    else:
        return Response({'Failed to update Rating'}, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_rating(request, pk):
    ratings = get_object_or_404(Rating, id=pk)
    if ratings.User.id == request.user.id:
        ratings.delete()
        return Response({'Rating successfully deleted'}, status.HTTP_204_NO_CONTENT)
    else:
        return Response({"Can't remove someone else's rating"}, status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_book_by_rating(request, book_amount):
    ratings = Rating.objects.annotate(title=F('book__title')).values('title').annotate(avg_rating=Avg("bookRating")).order_by('-avg_rating')[:book_amount]

    return Response(ratings)
