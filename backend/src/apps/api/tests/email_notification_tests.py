from django.test import TestCase, override_settings

from ...core.tasks import email_notification


class NotificationTest(TestCase):
    @override_settings(CELERY_ALWAYS_EAGER=True)
    def test_correct_notification_case(self):
        email_send_data = {
            "first_name": "test_name",
            "last_name": "test_name",
            "email": "testmail.com",
        }
        self.assertTrue(email_notification(email_send_data))

    @override_settings(CELERY_ALWAYS_EAGER=True)
    def test_notification_required_fields_not_exist(self):
        email_send_data = {}

        self.assertFalse(email_notification(email_send_data))
