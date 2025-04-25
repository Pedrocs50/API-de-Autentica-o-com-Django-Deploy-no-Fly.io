from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignupView, MeView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', MeView.as_view(), name='me'),
]
