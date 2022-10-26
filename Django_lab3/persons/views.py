from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User


# Register API
class UserController(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            "user": serializer.data
        })

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

    def put(self, request):
        if request.data.get('id') is not None:
            user = User.objects.get(pk=request.data.get('id'))
            if user:
                serializer = UserSerializer(user, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'success': True,
                        'message': 'APIView: updated blog post',
                        "user": serializer.data
                    })

    def delete(self, request):
        if request.data.get('id') is not None:
            user = User.objects.get(pk=request.data.get('id'))
            if user:
                user.delete()
                return Response({
                    'success': True,
                    'message': 'Successfully deleted User'
                })