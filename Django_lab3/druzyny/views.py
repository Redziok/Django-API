from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Druzyna
from .serializers import DruzynaSerializer

@api_view(['GET','POST'])
def getDruzyna(request):
    if request.method == 'GET':
        druzyny = Druzyna.objects.all()
        serializer = DruzynaSerializer(druzyny, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DruzynaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Successfully added Druzyna to database'}, status.HTTP_201_CREATED)
        else:
            return Response({'Failed to add Druzyna to database'}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def druzynaDetail(request, pk):
    try:
        druzyna = Druzyna.objects.get(id=pk)
    except Druzyna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DruzynaSerializer(druzyna, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DruzynaSerializer(druzyna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Successfully updated Druzyna'}, status.HTTP_201_CREATED)
        else:
            return Response({'Failed to update Druzyna'}, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        druzyna.delete()
        return Response({'Druzyna successfully deleted'}, status.HTTP_204_NO_CONTENT)