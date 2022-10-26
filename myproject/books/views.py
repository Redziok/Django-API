from rest_framework import generics
from rest_framework.response import Response
from .serializers import BookSerializer
from base.models import Books


# Register API
class BookController(generics.GenericAPIView):
    serializer_class = BookSerializer

    def get(self, request):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({
            "book": serializer.data
        })

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return Response({
            "book": BookSerializer(book, context=self.get_serializer_context()).data
        })

    def put(self, request):
        if request.data.get('id') is not None:
            book = Books.objects.get(pk=request.data.get('id'))
            if book:
                serializer = BookSerializer(book, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'success': True,
                        'message': 'APIView: updated blog post',
                        "book": serializer.data
                    })

    def delete(self, request):
        if request.data.get('id') is not None:
            book = Books.objects.get(pk=request.data.get('id'))
            if book:
                book.delete()
                return Response({
                    'success': True,
                    'message': 'Successfully deleted Books'
                })