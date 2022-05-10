import uuid

from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from ...core.utils import is_valid_uuid
from ..models import User
from ..serializers import UserSerializer


class TestUserViewSet(APITestCase):
    def setUp(self):
        """
        Run before every test case
        """
        self.fake = Faker()
        self.user = User.objects.create(
            id=uuid.uuid4(),
            first_name="test_user_first_name",
            last_name="test_user_last_name",
            email="test_user@mail.com",
        )

        self.client = APIClient()

    def test_list_users(self):
        """
        Test list users
        Permission : anyone
        """
        # GET /users/

        # 1. Users exist
        url = reverse("users-list")
        User.objects.bulk_create(
            [
                User(first_name=self.fake.first_name(), last_name=self.fake.last_name(), email=self.fake.email())
                for _ in range(4)
            ]
        )

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 5)

        # 2. Users not exist
        User.objects.all().delete()

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # In this case should be return 200 status code
        self.assertEqual(len(response.json()), 0)
        self.assertEqual(response.json(), list())

    def test_retrieve_user(self):
        """
        Test retrieve user
        Permission : anyone
        """
        # GET /users/{pk:uuid}

        # 1. Not exist
        url = f"/api/users/{uuid.uuid4()}/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # 2. Exist user
        url = f"/api/users/{self.user.id}/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["first_name"], self.user.first_name)
        self.assertEqual(response.json()["last_name"], self.user.last_name)
        self.assertEqual(response.json()["email"], self.user.email)

    def test_create_user(self):
        """
        Test create user
        Permission : anyone
        """
        # POST /users/
        url = reverse("users-list")

        # 1. Required fields are not filled
        user_required_fields = (
            ("first_name", "first_name_create"),
            ("last_name", "last_name_create"),
            ("email", "email_create@gmail.com"),
        )
        for field, value in user_required_fields:
            response = self.client.post(url, {field: value}, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 2. Correct request
        user_data = dict(user_required_fields)

        response = self.client.post(url, user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(is_valid_uuid(response.json()["id"]))

        self.assertEqual(response.json()["first_name"], user_data["first_name"])
        self.assertEqual(response.json()["last_name"], user_data["last_name"])
        self.assertEqual(response.json()["email"], user_data["email"])

    def test_update_user(self):
        """
        Test update user
        Permission : anyone
        """
        # PUT /users/{pk:uuid}

        url = f"/api/users/{self.user.pk}/"

        # 1. Required fields are not filled
        user_required_fields = (
            ("first_name", self.fake.first_name()),
            ("last_name", self.fake.last_name()),
            ("email", self.fake.email()),
        )
        for field, value in user_required_fields:
            response = self.client.put(url, {field: value}, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 2. Correct request
        updated_name = self.fake.first_name()
        user_data = UserSerializer(self.user).data
        user_data["first_name"] = updated_name

        response = self.client.put(url, user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["first_name"], updated_name)

        # response = self.client.put(url, "")

    def test_partial_update_user(self):
        """
        Test partial update user
        Permission : anyone
        """
        # PATCH /users/{pk:uuid}

        url = f"/api/users/{self.user.pk}/"

        updated_name = self.fake.first_name()

        response = self.client.patch(url, {"first_name": updated_name}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["first_name"], updated_name)
