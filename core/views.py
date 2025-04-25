from rest_framework import generics, permissions
from .serializers import SignupSerializer, UserSerializer
from .models import User
from rest_framework.response import Response

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

class MeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
