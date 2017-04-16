

from .models import Student
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import StudentSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def student_list(request):

    if request.method == 'GET':
        carts = Student.objects.all()
        serializer = StudentSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_id(request, pk):

    try:
        part = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






















