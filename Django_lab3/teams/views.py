from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from base.models import Team
from .serializers import TeamSerializer


@api_view(['GET', 'POST'])
def get_team(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Successfully added Team to database'}, status.HTTP_201_CREATED)
        else:
            return Response({'Failed to add Team to database'}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def team_detail(request, pk):
    try:
        person = Team.objects.get(id=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeamSerializer(person)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def team_update_delete(request, pk):
    try:
        person = Team.objects.get(id=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TeamSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Successfully updated Team'}, status.HTTP_201_CREATED)
        else:
            return Response({'Failed to update Team'}, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response({'Team successfully deleted'}, status.HTTP_204_NO_CONTENT)
