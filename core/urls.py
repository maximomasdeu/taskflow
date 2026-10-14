from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from core.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"projects", views.ProjectViewSet, basename="project")
router.register(r"tasks", views.TaskViewSet, basename="task")

urlpatterns = [
    path("health/", views.health_check, name="health_check"),
    path("", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/register/", RegisterView.as_view(), name="register"),
]

