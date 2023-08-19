from django.test import TestCase
from rest_framework.test import APIClient


class MyApiTestCase(TestCase):
    def setup(self):
        self.client=APIClient

    def myApiView(self):
        response = self.client.get('/myapi')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Success'})

# Create your tests here.
