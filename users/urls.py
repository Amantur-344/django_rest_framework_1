from django.urls import path
from .views import AccountRegisterAPIView, AccountRetrieveUpdateView

urlpatterns = [
    path('register/', AccountRegisterAPIView.as_view(), name='register'),
    path('<int:pk>/', AccountRetrieveUpdateView.as_view(), name='detail'),
    # path('user-detail/', CurrentUserView.as_view()),
    # path('users/<int:pk>/', UserDetail.as_view()),
]
