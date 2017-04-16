

from .models import Sports, Library
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SportsSerializer, LibrarySerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def sports_list(request):

    if request.method == 'GET':
        carts = Sports.objects.all()
        serializer = SportsSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SportsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def sports_id(request, pk):

    try:
        part = Sports.objects.get(pk=pk)
    except Sports.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SportsSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SportsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def library_list(request):

    if request.method == 'GET':
        carts = Library.objects.all()
        serializer = LibrarySerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def library_id(request, pk):

    try:
        part = Library.objects.get(pk=pk)
    except Library.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LibrarySerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




















