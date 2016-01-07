from django.test import TestCase

from accounts.models import User

from .models import Fine


class FineModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user(
                    email='test_email@gmail.com',
                    first_name='Test',
                    last_name='Case',
                    password='123456')

        Fine.objects.create(
            user=user,
            amount=20,
            status='UNPAID',
            reason='This is a test fine')

        Fine.objects.create(
            user=user,
            amount=30,
            status='UNPAID',
            reason='This is a test fine')
