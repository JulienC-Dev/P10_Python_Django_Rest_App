from django.urls import path
from .views import SignUpAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('signup/', SignUpAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]
