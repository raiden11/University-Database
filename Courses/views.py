
from .models import Course
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CourseSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def course_list(request):

    if request.method == 'GET':
        carts = Course.objects.all()
        serializer = CourseSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def course_id(request, pk):

    try:
        part = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
















