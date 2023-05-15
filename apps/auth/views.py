from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()

class AuthRegisterView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class AuthMeView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get_object(self):
        return self.request.user


