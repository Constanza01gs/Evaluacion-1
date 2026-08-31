from django.shortcuts import render
from rest_framework import viewsets

from .models import Teacher, Course, Student, StudentCourse
from .serializers import (
    TeacherSerializer,
    CourseSerializer,
    StudentSerializer,
    StudentCourseSerializer
)


# ============================================
# VISTAS HTML
# ============================================

# Página principal del sistema.
def home(request):
    return render(request, 'academic/home.html')


# Página de asignaturas.
def courses_view(request):
    return render(request, 'academic/courses.html')


# Página de estudiantes.
def students_view(request):
    return render(request, 'academic/students.html')


# ============================================
# ENDPOINTS DE DJANGO REST FRAMEWORK
# ============================================

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer