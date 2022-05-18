import datetime
import uuid

from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from ..models import Box, Questionary, User


class TestBoxQuestionaryViewSet(APITestCase):
    def setUp(self):
        """
        Run before every test case
        """
        self.fake = Faker()
        box_manager = User.objects.create(
            first_name=self.fake.first_name(), last_name=self.fake.last_name(), email=self.fake.email()
        )
        self.box = Box.objects.create(
            title=self.fake.iban(),
            price_range=12,
            last_join_data=datetime.date.today(),
            member_entry_message=self.fake.iban,
            manager=box_manager,
        )
        self.questionary_maker = User.objects.create(
            first_name=self.fake.first_name(), last_name=self.fake.last_name(), email=self.fake.email()
        )
        self.questionary = Questionary.objects.create(
            to_box=self.box, maker=self.questionary_maker, content=self.fake.paragraph(nb_sentences=5)
        )

        self.client = APIClient()

    def test_box_questionnaires_list__not_exist_box(self):
        """
        Test box questionnaires
        Permission : anyone
        """
        # GET /boxes/{pk:uuid}/questionnaires/

        url = reverse("boxes-questionnaires", kwargs={"pk": uuid.uuid4()})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_box_questionnaires_list(self):
        """
        Test box questionnaires list
        Permission : anyone
        """
        # GET /boxes/{pk:uuid}/questionnaires/

        url = reverse("boxes-questionnaires", kwargs={"pk": self.box.pk})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.json(), list))
        self.assertEqual(len(response.json()), Questionary.objects.filter(to_box=self.box).count())

    def test_box_questionnaires_retrieve__exist_questionary(self):
        """
        Test box detail questionary
        Permission : anyone
        """
        # GET /boxes/{pk:uuid}/questionnaires/{questionary_id:int}/

        url = reverse("boxes-questionary-detail", kwargs={"pk": self.box.pk, "questionary_id": self.questionary.pk})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["content"], self.questionary.content)

    def test_box_questionnaires_retrieve__not_exist_questionary(self):
        """
        Test box detail questionary not exist
        Permission : anyone
        """
        # GET /boxes/{pk:uuid}/questionnaires/{questionary_id:int}/

        url = reverse("boxes-questionary-detail", kwargs={"pk": self.box.pk, "questionary_id": self.questionary.pk})
        Questionary.objects.all().delete()

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_box_questionnaires_create(self):
        """
        Test box questionary create
        Permission : anyone
        """
        # POST /boxes/{pk:uuid}/questionnaires/

        url = reverse("boxes-questionnaires", kwargs={"pk": self.box.pk})

        questionary_data = {
            "maker": {
                "first_name": self.fake.first_name(),
                "last_name": self.fake.last_name(),
                "email": self.fake.email(),
            },
            "content": self.fake.paragraph(nb_sentences=5),
        }

        response = self.client.post(url, data=questionary_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(isinstance(response.json(), dict))
        self.assertEqual(response.json()["content"], questionary_data["content"])

    def test_box_questionnaires_create__failed(self):
        """
        Test box questionary create failed case
        Permission : anyone
        """
        # POST /boxes/{pk:uuid}/questionnaires/

        url = reverse("boxes-questionnaires", kwargs={"pk": self.box.pk})

        questionary_data = {
            "maker": {
                "first_name": self.fake.first_name(),
                "last_name": self.fake.last_name(),
            },
            "content": self.fake.paragraph(nb_sentences=5),
        }

        response = self.client.post(url, data=questionary_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_box_questionary_delete(self):
        """
        Test box questionary delete case
        Permission : anyone
        """
        # DELETE /boxes/{pk:uuid}/questionnaires/{questionary_id:int}/

        url = reverse("boxes-questionary-detail", kwargs={"pk": self.box.pk, "questionary_id": self.questionary.pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Questionary.objects.filter(id=self.questionary.id).count())

    def test_box_questionary_delete__not_exist_questionary(self):
        """
        Test box questionary delete case
        Permission : anyone
        """
        # DELETE /boxes/{pk:uuid}/questionnaires/{questionary_id:int}/

        url = reverse("boxes-questionary-detail", kwargs={"pk": self.box.pk, "questionary_id": self.questionary.pk})
        Questionary.objects.all().delete()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_box_questionary_update(self):
        """
        Test box questionary update case
        Permission : anyone
        """
        # PUT /boxes/{pk:uuid}/questionnaires/{questionary_id:int}/

        url = reverse("boxes-questionary-detail", kwargs={"pk": self.box.pk, "questionary_id": self.questionary.pk})

        update_data = {"content": "Some text"}
        response = self.client.put(url, update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["content"], update_data["content"])

    def test_box_questionary_partial_update(self):
        """
        Test box questionary partial update case
        Permission : anyone
        """
        # PATCH /boxes/{pk:uuid}/questionnaires/{questionary_id:int}/

        url = reverse("boxes-questionary-detail", kwargs={"pk": self.box.pk, "questionary_id": self.questionary.pk})

        update_data = {"content": "Some text"}
        response = self.client.patch(url, update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["content"], update_data["content"])
