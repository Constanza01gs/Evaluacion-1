from django.db import models


# ============================================
# MODELO: DOCENTE
# ============================================
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ============================================
# MODELO: ASIGNATURA
# ============================================
class Course(models.Model):
    name = models.CharField(max_length=100)

    # Cada curso pertenece a un docente.
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    def __str__(self):
        return self.name


# ============================================
# MODELO: ESTUDIANTE
# ============================================
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ============================================
# MODELO: INSCRIPCIÓN
# ============================================
class StudentCourse(models.Model):
    # Relación entre estudiante y curso.
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    class Meta:
        # Evita que un estudiante se inscriba
        # dos veces en el mismo curso.
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} - {self.course}"