from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views_api import ProductDetailView, ProductListView, RegisterApi
from .doc import urlpatterns as urlp
from vova_project import settings
from .serializers import CustomJWTSerializer


urlpatterns = [
    path('api/register', RegisterApi.as_view()),
    path('api/', ProductListView.as_view()),
    path('api/<int:pk>/', ProductDetailView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += urlp