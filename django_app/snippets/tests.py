from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from snippets.models import Snippet


class SnippetTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new snippet object.
        """
        url = reverse('snippets:list')
        data = {'code':'url()',
                'title': 'test-snippet',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 1)
        self.assertEqual(Snippet.objects.get().title, 'test-snippet')