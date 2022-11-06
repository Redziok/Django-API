from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from knox.models import AuthToken
from .serializers import UserAddSerializer, UserSerializer

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserAddSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=UserAddSerializer.context).data,
        "token": AuthToken.objects.create(user)[1]
    })
    else:
        return Response({'Failed to add User to database'},status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateUser(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserAddSerializer(users, data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        password = AuthToken.objects.create(user)[1]
        user.password = password
        return Response({
        "user": UserSerializer(user, context=UserAddSerializer.context).data,
        "token": AuthToken.objects.create(user)[1]
    })
    else:
        return Response({'Failed to update User'},status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    if user.is_superuser==True: 
        return Response({"Can't delete superuser"},status.HTTP_400_BAD_REQUEST)
    else:
        user.delete()
        return Response({'User successfully deleted'}, status.HTTP_204_NO_CONTENT)