from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from . import models


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Materia
        fields = ['id', 'name', 'description']


class EnrollmentSerializer(serializers.ModelSerializer):
    materia = MateriaSerializer(many=False, read_only=True)
    class Meta:
        model = models.Enrollment
        fields = ['id', 'student', 'materia', 'state']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    # enrollments = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='api_v2:enrollment-detail')
    enrollments = EnrollmentSerializer(many=True, read_only=True)

    class Meta:
        model = models.Student
        fields = ['id', 'user', 'curso', 'enrollments']