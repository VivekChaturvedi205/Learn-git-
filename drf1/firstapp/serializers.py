from rest_framework import serializers
from .models import student

# class Studentserializer(serializers.ModelSerializer):
#     class Meta:
#         model=student
#         fields='__all__'

# class Studentserializer(serializers.Serializer):
#     Name=serializers.CharField(max_length=15)
#     Roll_no=serializers.IntegerField()
#     City=serializers.CharField(max_length=20)

class Studentserializer(serializers.Serializer):
    Name=serializers.CharField(max_length=15)
    Roll_no=serializers.IntegerField()
    City=serializers.CharField(max_length=20)

    def create(self, validated_data):
        return student.objects.create(**validated_data)