from django.urls import path, include
from . views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('user', UserView.as_view()),
    path('login', MyTokenObtainPairView.as_view()),
    path('validate', TokenRefreshView.as_view()),
    path('user/deposit', UserDepositView.as_view()),
    path('user/reset', DepositResetView.as_view()),
]