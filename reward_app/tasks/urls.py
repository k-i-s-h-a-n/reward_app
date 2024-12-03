from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppViewSet, TaskViewSet, UserViewSet
from . views import *

router = DefaultRouter()
router.register('apps', AppViewSet)
router.register('tasks', TaskViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admind',admin,name="admin"),
]
