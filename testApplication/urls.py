from django.urls import path, include
from .views import health_check, Subject, Student
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    'subject',
    Subject,
    basename="subject"
)

router.register(
    'student',
    Student,
    basename="student"
)


urlpatterns = [
    path('health/', health_check, name='health_check'),
    path(r'api/v1/', include(router.urls), name='api'),
]