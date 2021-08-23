from django.urls import path, include
from rest_framework import routers

from .api import NoteViewSet

router = routers.DefaultRouter()
router.register('note', NoteViewSet, 'note')

urlpatterns = [
    path('api/', include(router.urls))
]