
from rest_framework import serializers
from Facilities.models import Sports, Library


class SportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sports
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = '__all__'






