from rest_framework import generics
from rest_framework.response import Response
from .serializers import AuthorSerializer
from base.models import Authors


# Register API
class AuthorController(generics.GenericAPIView):
    serializer_class = AuthorSerializer

    def get(self, request):
        authors = Authors.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({
            "author": serializer.data
        })

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.save()
        return Response({
            "author": AuthorSerializer(author, context=self.get_serializer_context()).data
        })

    def put(self, request):
        if request.data.get('id') is not None:
            author = Authors.objects.get(pk=request.data.get('id'))
            if author:
                serializer = AuthorSerializer(author, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'success': True,
                        'message': 'APIView: updated blog post',
                        "author": serializer.data
                    })

    def delete(self, request):
        if request.data.get('id') is not None:
            author = Authors.objects.get(pk=request.data.get('id'))
            if author:
                author.delete()
                return Response({
                    'success': True,
                    'message': 'Successfully deleted Author'
                })