from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'classes', views.ClassViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'grades', views.GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
