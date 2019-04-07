from django.test import TestCase
from django.urls import reverse
from .models import SpaceSignal
from rest_framework.test import APITestCase
from django.utils import timezone
from rest_framework import status


class SpaceSignalModelTest(TestCase):
    def setUp(self):
        SpaceSignal.objects.create(publish_date=timezone.datetime(2019, 1, 1), system='Sol', content='Hello Worlds!',
                                   author='God')
        SpaceSignal.objects.create(publish_date=timezone.datetime(2019, 1, 2), system='Sol',
                                   content='Hello again Worlds!', author='God')

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


class APIPostTest(APITestCase):
    def test_post_request_correct(self):
        url = reverse('signals')
        data = {'author': 'Darth Vader',
                'system': 'Alpha Centauri',
                'content': 'I see through the lies of the Jedi.'
                }
        response = self.client.post(path=url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(SpaceSignal.objects.get())

        data = {'author': 'Darth Vader',
                'system': 'Alpha Centauri',
                'content': 'I see through the lies of the Jedi.',
                'publish_date': timezone.now()
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SpaceSignal.objects.all().count(), 2)

    def test_post_request_incorrect(self):
        url = reverse('signals')
        data = {'system': 'Alpha Centauri',
                'content': 'I see through the lies of the Jedi.'
                }
        response = self.client.post(path=url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {'author': 'Darth Vader',
                'anotherfield': 'Alpha Centauri',
                'content': 'I see through the lies of the Jedi.',
                'publish_date': timezone.datetime(2019, 1, 1, 1, 30)
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(SpaceSignal.objects.all().count(), 0)


class APIListTest(APITestCase):
    def setUp(self):
        SpaceSignal.objects.create(publish_date=timezone.datetime(2019, 1, 1), system='Sol', content='Hello Worlds!',
                                   author='God')
        SpaceSignal.objects.create(publish_date=timezone.datetime(2019, 1, 2), system='Sol',
                                   content='Hello again Worlds!', author='God')

    def test_list_request_correct(self):
        url = reverse('signals')
        data = {'system': 'Sol'}
        response = self.client.get(path=url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0].get('system'), 'Sol')


    def test_list_request_incorrect(self):
        url = reverse('signals')
        data = {'randomattr': 'Sol'}
        response = self.client.get(path=url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

