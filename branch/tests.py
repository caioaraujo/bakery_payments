from rest_framework import status
from rest_framework.test import APITestCase

from branch.exceptions import LargeNameException


class TestsUsecase(APITestCase):

    def setUp(self):
        self.BASE_URL = '/branches/'

    def test_post__success(self):
        data = {'name': 'Padaria C'}
        response = self.client.post(self.BASE_URL, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('id') > 0)

    def test_post__large_name(self):
        data = {'name': 'Padaria de muitos caractereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees'}
        with self.assertRaises(LargeNameException):
            self.client.post(self.BASE_URL, data)

