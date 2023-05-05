from django.urls import path
from . import views
from . import events
from . import tokens
# from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


app_name = 'api'

urlpatterns = [
    # Common endpoints
    path("", views.index, name="api_index"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Events endpoints
    path("events/", events.index, name="events_index"),
    # Tokens endpoints
    path("tokens/", tokens.index, name="tokens_index"),
]
