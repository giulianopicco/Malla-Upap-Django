from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save


class Student(models.Model):
    PRIMER, SEGUNDO, TERCERO, CUARTO, QUINTO = range(5)
    CURSOS = [
        (PRIMER, 'Primer curso'),
        (SEGUNDO, 'Segundo curso'),
        (TERCERO, 'Tercero curso'),
        (CUARTO, 'Cuarto curso'),
        (QUINTO, 'Quinto curso'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    curso = models.IntegerField(choices=CURSOS, default=PRIMER)

    def __str__(self):
        return self.user.username


def save_student(sender, instance, **kwargs):
    materias = Materia.objects.all()
    for materia in materias:
        enrollment = Enrollment.objects.create(
            student=instance,
            materia=materia,
        )


post_save.connect(save_student, sender=Student)


class Materia(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    PENDIENTE, CURSANDO, APROBADO, APLAZADO = range(4)
    STATES = [
        (PENDIENTE, 'Pendiente'),
        (CURSANDO, 'Cursando'),
        (APROBADO, 'Aprobado'),
        (APLAZADO, 'Aplazado'),
    ]
    student = models.ForeignKey(Student, related_name="enrollments", on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, related_name="enrollments", on_delete=models.CASCADE)
    state = models.IntegerField(choices=STATES, default=PENDIENTE)

    class Meta:
        unique_together = [['student', 'materia']]

    def __str__(self):
        return 'student: {} - materia {}'.format(self.student.user.username, self.materia.name)