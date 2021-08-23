from .models import Note
from rest_framework import viewsets, permissions
from .serializers import NoteSerializer

# 게시판 ViewSet
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # def get_queryset(self):
    #     return self.request.user.note.all()

    # def create_note(self, serializer):
    #     serializer.save()

