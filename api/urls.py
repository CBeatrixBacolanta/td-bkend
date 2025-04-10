from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todo')
urlpatterns = [
    path('', include(router.urls)),
]