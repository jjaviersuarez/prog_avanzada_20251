from django.db import models

# Create your models here.


#modelo para los cursos
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    alumnos = models.ManyToManyField('Alumno', related_name='cursos')

    def __str__(self):
        return self.nombre

#modelo para los alumnos
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    cursos = models.ManyToManyField(Curso, related_name='alumnos')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#modelo para los profesores
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    cursos = models.ManyToManyField(Curso, related_name='profesores')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
