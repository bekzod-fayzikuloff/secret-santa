from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Box, User
from .serializers import (
    BoxCreateSerializer,
    BoxListSerializer,
    BoxMemberJoinSerializer,
    BoxRetrieveSerializer,
    BoxUpdateSerializer,
    UserSerializer,
)


@api_view()
def index(request):
    return Response("test")


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BoxViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Box.objects.all()
    serializer_class = BoxListSerializer

    @action(methods=["POST"], detail=True, serializer_class=BoxMemberJoinSerializer)
    def join(self, request, pk):
        box = get_object_or_404(Box, pk=pk)
        serializer = self.serializer_class(data=self.request.POST)

        if serializer.is_valid():
            new_member = serializer.save()
            box.members.add(new_member)
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        actions = {
            "list": BoxListSerializer,
            "retrieve": BoxRetrieveSerializer,
            "create": BoxCreateSerializer,
            "update": BoxUpdateSerializer,
        }
        return actions.get(self.action, self.serializer_class)
