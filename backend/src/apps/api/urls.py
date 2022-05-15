from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet, basename="users")
router.register(r"boxes", views.BoxViewSet, basename="boxes")

urlpatterns = []

urlpatterns += router.urls
