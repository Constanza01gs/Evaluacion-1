from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


# ============================================
# ROUTER DE LA API
# ============================================

router = DefaultRouter()

router.register(r'teachers', views.TeacherViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'student-courses', views.StudentCourseViewSet)


# ============================================
# RUTAS DE LA APLICACIÓN
# ============================================

urlpatterns = [

    # Página principal
    path('', views.home, name='home'),

    # Vistas HTML
    path('courses/', views.courses_view, name='courses'),
    path('students/', views.students_view, name='students'),

    # API consumida internamente con fetch()
    path('api/', include(router.urls)),
]