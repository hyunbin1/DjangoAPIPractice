from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth.models import User
from .models import Profile

from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, ProfileSerializer

#Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()

        return Response(
            {
              "user": UserSerializer(user, context = self.get_serializer_context()). data,
              "token": AuthToken.objects.create(user)[1] # token은 헤더에 들어가며, 사용자 정보를 알려준다.
            }
        )

# Login API
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.validated_data

      return Response(
          { "user": UserSerializer(user, context = self.get_serializer_context()).data, 
            "token": AuthToken.objects.create(user)[1] # token은 헤더에 들어가며, 사용자 정보를 알려준다.   
          }
      )
  

# GET User API
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [permissions.IsAuthenticated,]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user

# GET UserList API
class UserListAPI(viewsets.ViewSet):
      def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many = True)
        return Response(serializer.data)


# CreateProfile
class CreateProfileAPI(generics.GenericAPIView):
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()

        return Response(
            {
              "user": ProfileSerializer(user, context = self.get_serializer_context()). data,
            }
        )

# Get Profile API
class ProfileListAPI(viewsets.ViewSet):
      def list(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many = True)
        return Response(serializer.data)
