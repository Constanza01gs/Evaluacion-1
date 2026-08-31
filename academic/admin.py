from django.contrib import admin
from .models import Teacher, Course, Student, StudentCourse


# ============================================
# ADMINISTRACIÓN DE DOCENTES
# ============================================
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


# ============================================
# ADMINISTRACIÓN DE ASIGNATURAS
# ============================================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher')
    search_fields = ('name',)
    list_filter = ('teacher',)


# ============================================
# ADMINISTRACIÓN DE ESTUDIANTES
# ============================================
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


# ============================================
# ADMINISTRACIÓN DE INSCRIPCIONES
# ============================================
@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')
    list_filter = ('course',)