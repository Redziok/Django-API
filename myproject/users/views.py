from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from knox.models import AuthToken
from .serializers import UserAddSerializer, UserSerializer

@api_view(['GET'])
def Get_Users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Get_User(request, pk):
    user = get_object_or_404(User, id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Add_User(request):
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
def Update_User(request, pk):
    author = get_object_or_404(User, id=pk)
    serializer = UserAddSerializer(author, data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return Response({'Successfully updated User'},status.HTTP_201_CREATED)
    else:
        return Response({'Failed to update User'},status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, permissions])
def Delete_User(request, pk):
    user = get_object_or_404(User, id=pk)
    if user.is_superuser==True: 
        return Response({"Can't delete superuser"},status.HTTP_400_BAD_REQUEST)
    else:
        user.delete()
        return Response({'User successfully deleted'}, status.HTTP_204_NO_CONTENT)