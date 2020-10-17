from rest_framework import viewsets

from materia import models
from . import serializers


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = models.Materia.objects.all()
    serializer_class = serializers.MateriaSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = models.Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer
