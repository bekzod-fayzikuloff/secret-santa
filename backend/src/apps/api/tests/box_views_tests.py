import datetime
import uuid

from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from ..models import Box, User
from ..serializers import BoxUpdateSerializer


class TestBoxViewSet(APITestCase):
    def setUp(self):
        """
        Run before every test case
        """
        self.fake = Faker()
        self.box_manager = User.objects.create(
            first_name=self.fake.first_name(), last_name=self.fake.last_name(), email=self.fake.email()
        )
        self.box = Box.objects.create(
            title=self.fake.iban(),
            price_range=12,
            last_join_data=datetime.date.today(),
            member_entry_message=self.fake.iban,
            manager=self.box_manager,
        )

        self.client = APIClient()

    def test_list_box__boxes_exist(self):
        """
        Test list boxes exist case
        Permission : anyone
        """
        # GET /boxes/

        url = reverse("boxes-list")
        response = self.client.get(url)
        box_quantity = Box.objects.count()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), box_quantity)
        self.assertTrue(isinstance(response.json(), list))

    def test_list_box__empty_qs(self):
        """
        Test list boxes not exist case, empty queryset
        Permission : anyone
        """
        # GET /boxes/

        url = reverse("boxes-list")
        Box.objects.all().delete()
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 0)
        self.assertTrue(isinstance(response.json(), list))

    def test_retrieve_box__exist_box(self):
        """
        Test retrieve box
        Permission : anyone
        """
        # GET /boxes/{pk:uuid}

        url = reverse("boxes-detail", kwargs={"pk": self.box.pk})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.json(), dict))

    def test_retrieve_box__not_exist_box(self):
        """
        Test retrieve not exist box
        Permission : anyone
        """
        # GET /boxes/{pk:uuid}

        url = reverse("boxes-detail", kwargs={"pk": uuid.uuid4()})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn(response.json()["detail"], "Not found.")

    def test_update_box__not_exist_box(self):
        """
        Test update box
        Permission : anyone
        """
        # PUT /boxes/{pk:uuid}

        url = reverse("boxes-detail", kwargs={"pk": uuid.uuid4()})

        response = self.client.put(url, data={"some_field": self.fake.iban()})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn(response.json()["detail"], "Not found.")

    def test_update_box__not_fill_required_fields(self):
        """
        Test update box
        Permission : anyone
        """
        # PUT /boxes/{pk:uuid}

        url = reverse("boxes-detail", kwargs={"pk": self.box.pk})

        response = self.client.put(url, data={"some_field": self.fake.iban()})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_box__fill_all_required_fields(self):
        """
        Test update box
        Permission : anyone
        """
        # PUT /boxes/{pk:uuid}

        url = reverse("boxes-detail", kwargs={"pk": self.box.pk})
        box_fields = BoxUpdateSerializer(self.box)

        changed_box = box_fields.data
        changed_box["title"] = "new_title"

        response = self.client.put(url, data=changed_box)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], "new_title")

    def test_partial_update_box__not_exist_box(self):
        """
        Test partial update box
        Permission : anyone
        """
        # PATCH /boxes/{pk:uuid}

        url = reverse("boxes-detail", kwargs={"pk": uuid.uuid4()})

        response = self.client.put(url, data={"title": self.fake.iban()})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_partial_update_box__exist_field_change(self):
        """
        Test partial update box
        Permission : anyone
        """
        # PATCH /boxes/{pk:uuid}

        url = reverse("boxes-detail", kwargs={"pk": self.box.pk})

        response = self.client.patch(url, data={"title": "new_title"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], "new_title")

    def test_destroy_box__exist_box(self):
        """
        Test destroy exist box
        Permission : anyone
        """
        # DELETE /boxes/{pk:uuid}
        url = reverse("boxes-detail", kwargs={"pk": self.box.pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_destroy_box__not__exist_box(self):
        """
        Test destroy not exist box
        Permission : anyone
        """
        # DELETE /boxes/{pk:uuid}
        url = reverse("boxes-detail", kwargs={"pk": uuid.uuid4()})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_join_action_view__not_exist_box(self):
        """
        Test `join action` not exist box
        Permission : anyone
        """
        # POST /boxes/{pk:uuid}/join/

        url = reverse("boxes-join", kwargs={"pk": uuid.uuid4()})

        response = self.client.post(url, dict())

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_join_action_view__exist_box_invalid_post_request(self):
        """
        Test `join action` exist box
        Permission : anyone
        """
        # POST /boxes/{pk:uuid}/join/

        url = reverse("boxes-join", kwargs={"pk": self.box.pk})

        response = self.client.post(url, dict())

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_join_action_view__exist_box_valid_post_request(self):
        """
        Test `join action` exist box
        Permission : anyone
        """
        # POST /boxes/{pk:uuid}/join/

        url = reverse("boxes-join", kwargs={"pk": self.box.pk})

        member_data = {
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "email": self.fake.email(),
        }
        response = self.client.post(url, member_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
