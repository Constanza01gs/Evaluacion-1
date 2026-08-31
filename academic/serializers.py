from rest_framework import serializers
from .models import Teacher, Course, Student, StudentCourse


# ============================================
# SERIALIZADOR DE DOCENTES
# ============================================
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


# ============================================
# SERIALIZADOR DE ASIGNATURAS
# ============================================
class CourseSerializer(serializers.ModelSerializer):
    # Mostramos además el nombre completo del docente.
    teacher_name = serializers.CharField(
        source='teacher.__str__',
        read_only=True
    )

    class Meta:
        model = Course
        fields = '__all__'


# ============================================
# SERIALIZADOR DE ESTUDIANTES
# ============================================
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# ============================================
# SERIALIZADOR DE INSCRIPCIONES
# ============================================
class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'