from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet, basename="users")

urlpatterns = [path("", views.index)]

urlpatterns += router.urls
