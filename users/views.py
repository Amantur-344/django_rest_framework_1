from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsOwner
from .serializers import AccountRegistrationSerializer, AccountDetailSerializer
from .models import Account
from rest_framework import generics, permissions


class AccountRegisterAPIView(generics.CreateAPIView):
    serializer_class = AccountRegistrationSerializer
    permission_classes = (permissions.AllowAny, )


class AccountRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)


# class CurrentUserView(APIView):
#     def get(self, request):
#         serializer = AccountSerializer(request.user)
#         return Response(serializer.data)
#
#
# class UserDetail(generics.RetrieveUpdateAPIView):
#     serializer_class = AccountDetailSerializer
#     queryset = Account.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
