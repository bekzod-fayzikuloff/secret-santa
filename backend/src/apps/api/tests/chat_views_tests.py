import datetime
import uuid

from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from ..models import Box, Message, SecretChat, User


class TestBoxQuestionaryViewSet(APITestCase):
    def setUp(self):
        """
        Run before every test case
        """
        self.fake = Faker()
        box_manager = User.objects.create(
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            email=self.fake.email(),
        )
        self.box = Box.objects.create(
            title=self.fake.iban(),
            price_range=10,
            last_join_data=datetime.date.today(),
            member_entry_message=self.fake.iban,
            manager=box_manager,
        )
        self.chat = SecretChat.objects.create(to_box=self.box)
        self.message = Message.objects.create(to_chat=self.chat, content="test_message")
        self.client = APIClient()

    def test_box_chat__exist_box(self):
        # GET /boxes/{pk:uuid}/chat/

        url = reverse("boxes-chat", kwargs={"pk": self.box.pk})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.json()["messages"]),
            Message.objects.filter(to_chat__to_box=self.box).count(),
        )

    def test_box_chat__not_exist_box(self):
        # GET /boxes/{pk:uuid}/chat/

        url = reverse("boxes-chat", kwargs={"pk": uuid.uuid4()})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_box_chat_message_create(self):
        # POST /boxes/{pk:uuid}/chat/

        url = reverse("boxes-chat", kwargs={"pk": self.box.pk})
        post_data = {"content": "new_message"}

        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["content"], post_data["content"])

    def test_box_chat_message_create__not_exist_box(self):
        # POST /boxes/{pk:uuid}/chat/

        url = reverse("boxes-chat", kwargs={"pk": uuid.uuid4()})

        response = self.client.post(url, {"content": "new_message"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_box_chat_message_create_failed_case(self):
        # POST /boxes/{pk:uuid}/chat/

        url = reverse("boxes-chat", kwargs={"pk": self.box.pk})

        response = self.client.post(
            url,
            {
                "some_field": "new_message",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_box_chat_message_retrieve(self):
        # GET /boxes/{pk:uuid}/chat/message/{message_id:int}/

        url = reverse(
            "boxes-message-detail",
            kwargs={"pk": self.box.pk, "message_id": self.message.pk},
        )

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_box_chat_message_update(self):
        # PUT /boxes/{pk:uuid}/chat/message/{message_id:int}/

        url = reverse(
            "boxes-message-detail",
            kwargs={"pk": self.box.pk, "message_id": self.message.pk},
        )

        put_data = {"content": "new_text"}
        response = self.client.put(url, put_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["content"], put_data["content"])

    def test_box_chat_message_update_failed_case(self):
        # PUT /boxes/{pk:uuid}/chat/message/{message_id:int}/

        url = reverse(
            "boxes-message-detail",
            kwargs={"pk": self.box.pk, "message_id": self.message.pk},
        )

        put_data = {"not_exist_field": "new_text"}
        response = self.client.put(url, put_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_box_chat_message_partial_update(self):
        # PATCH /boxes/{pk:uuid}/chat/message/{message_id:int}/

        url = reverse(
            "boxes-message-detail",
            kwargs={"pk": self.box.pk, "message_id": self.message.pk},
        )

        patch_data = {"content": "new_text"}
        response = self.client.patch(url, patch_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_box_chat_message_partial_update_failed_case(self):
        # PUT /boxes/{pk:uuid}/chat/message/{message_id:int}/

        url = reverse(
            "boxes-message-detail",
            kwargs={"pk": self.box.pk, "message_id": self.message.pk},
        )

        patch_data = {"not_exist_field": "new_text"}
        response = self.client.put(url, patch_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
