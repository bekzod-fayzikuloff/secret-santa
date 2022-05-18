import copy

from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from ..core.tasks import email_notification
from .models import Box, Message, Questionary, SecretChat, User
from .serializers import (
    BoxCreateSerializer,
    BoxListSerializer,
    BoxMemberJoinSerializer,
    BoxRetrieveSerializer,
    BoxUpdateSerializer,
    ChatSerializer,
    CreateMessageSerializer,
    ListQuestionarySerializer,
    RetrieveMessageSerializer,
    UpdateQuestionarySerializer,
    UserSerializer,
)


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
    def join(self, request: HttpRequest, pk: str) -> Response:
        box = get_object_or_404(Box, pk=pk)
        serializer = self.serializer_class(data=self.request.POST)

        if serializer.is_valid():
            new_member = serializer.save()
            box.members.add(new_member)

            message_data = copy.deepcopy(serializer.data)
            message_data["box_id"] = box.pk
            email_notification.delay(message_data)

            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["GET", "POST"], detail=True, serializer_class=ListQuestionarySerializer)
    def questionnaires(self, request: HttpRequest, pk: str) -> Response:
        box = get_object_or_404(self.queryset, pk=pk)

        if self.request.method == "POST":
            serializer = self.serializer_class(data=self.request.data)
            if serializer.is_valid():
                serializer.save(to_box=box)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        queryset = Questionary.objects.filter(to_box=box)
        questionary_list = self.serializer_class(queryset, many=True).data
        return Response(questionary_list)

    @action(
        methods=["GET", "PUT", "PATCH", "DELETE"],
        detail=True,
        url_path=r"questionnaires/(?P<questionary_id>\w+)",
        serializer_class=ListQuestionarySerializer,
    )
    def questionary_detail(self, request: HttpRequest, pk: str, questionary_id) -> Response:
        box = get_object_or_404(self.queryset, pk=pk)
        questionary = get_object_or_404(Questionary, to_box=box, pk=questionary_id)

        if self.request.method in ("PUT", "PATCH"):
            serializer = UpdateQuestionarySerializer(data=self.request.data)

            if serializer.is_valid():
                questionary.content = serializer.validated_data["content"]
                questionary.save()
                serialized_questionary = self.serializer_class(questionary).data
                return Response(serialized_questionary)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        if self.request.method == "DELETE":
            questionary.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        questionary_data = self.serializer_class(questionary).data
        return Response(questionary_data)

    @action(
        methods=["GET", "POST"],
        detail=True,
        serializer_class=CreateMessageSerializer,
    )
    def chat(self, request: HttpRequest, pk: str) -> Response:
        box = get_object_or_404(self.queryset, pk=pk)
        chat = get_object_or_404(SecretChat, to_box=box)

        if self.request.method == "POST":
            serializer = self.serializer_class(data=self.request.data)

            if serializer.is_valid():
                serializer.save(to_chat=chat, message_from=None)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        chat_data = ChatSerializer(chat).data

        return Response(chat_data)

    @action(
        methods=["GET", "PUT", "PATCH"],
        detail=True,
        url_path=r"chat/messages/(?P<message_id>\w+)",
        serializer_class=CreateMessageSerializer,
    )
    def message_detail(self, request: HttpRequest, pk: str, message_id) -> Response:
        chat = get_object_or_404(SecretChat, to_box_id=pk)
        message = get_object_or_404(Message, pk=message_id, to_chat=chat)

        if self.request.method in ("POST", "PUT"):
            serializer = self.serializer_class(data=self.request.data)
            if serializer.is_valid():
                message.content = serializer.validated_data["content"]
                message.save()
                message_data = CreateMessageSerializer(message).data
                return Response(message_data)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        message_data = RetrieveMessageSerializer(message).data
        return Response(message_data)

    def get_serializer_class(self):
        actions = {
            "list": BoxListSerializer,
            "retrieve": BoxRetrieveSerializer,
            "create": BoxCreateSerializer,
            "update": BoxUpdateSerializer,
        }
        return actions.get(self.action, self.serializer_class)
