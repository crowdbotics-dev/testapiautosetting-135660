from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135660ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135660", Testconnectors135660ViewSet, basename="testconnectors135660"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
