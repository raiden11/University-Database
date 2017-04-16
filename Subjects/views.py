

from .models import Subject
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SubjectSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def subject_list(request):

    if request.method == 'GET':
        carts = Subject.objects.all()
        serializer = SubjectSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def subject_id(request, pk):

    try:
        part = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


















