from django.test import TestCase
from .models import SpaceSignal
from rest_framework.test import APITestCase
from django.utils import timezone


class SpaceSignalModelTest(TestCase):
    def setUp(self):
        SpaceSignal.objects.create(publish_date=timezone.datetime(2019, 1, 1), system='Sol', content='Hello Worlds!', author='God')
        SpaceSignal.objects.create(publish_date=timezone.datetime(2019, 1, 2), system='Sol', content='Hello again Worlds!', author='God')

    def test_signals_created(self):
        self.assertEqual(SpaceSignal.objects.all().count(), 2)
        signal1 = SpaceSignal.objects.get(content='Hello Worlds!')
        self.assertEqual(signal1.system, 'Sol')
        self.assertEqual(signal1.author, 'God')

        signal2 = SpaceSignal.objects.get(content='Hello again Worlds!')
        self.assertEqual(signal2.system, 'Sol')
        self.assertEqual(signal2.author, 'God')

    def test_string_representation(self):
        self.fail('TODO')

    def test_object_delete(self):
        self.fail('TODO')

    def test_object_filtering(self):
        self.fail('TODO')


class APITest(APITestCase):
    pass