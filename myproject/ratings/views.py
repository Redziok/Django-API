from rest_framework import generics
from rest_framework.response import Response
from .serializers import RatingSerializer
from base.models import Ratings


# Register API
class RatingController(generics.GenericAPIView):
    serializer_class = RatingSerializer

    def get(self, request):
        ratings = Ratings.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response({
            "rating": serializer.data
        })

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating = serializer.save()
        return Response({
            "rating": RatingSerializer(rating, context=self.get_serializer_context()).data
        })

    def put(self, request):
        if request.data.get('id') is not None:
            rating = Ratings.objects.get(pk=request.data.get('id'))
            if rating:
                serializer = RatingSerializer(rating, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'success': True,
                        'message': 'APIView: updated blog post',
                        "rating": serializer.data
                    })

    def delete(self, request):
        if request.data.get('id') is not None:
            rating = Ratings.objects.get(pk=request.data.get('id'))
            if rating:
                rating.delete()
                return Response({
                    'success': True,
                    'message': 'Successfully deleted Rating'
                })