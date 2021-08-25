from .serializers import AccountRegistrationSerializer
from .models import Account
from rest_framework import generics


class AccountRegisterAPIView(generics.CreateAPIView):
    serializer_class = AccountRegistrationSerializer
