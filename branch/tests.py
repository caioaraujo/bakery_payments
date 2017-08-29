from rest_framework import status
from rest_framework.test import APITestCase

from branch.exceptions import LargeNameException, RequiredValueException


class BranchTestsUsecase(APITestCase):

    def setUp(self):
        self.BASE_URL = '/branches/'

    # ==================================================================================================================
    # Post
    # ==================================================================================================================

    def test_post__success(self):
        data = {'name': 'Padaria C', 'current_balance': 120000}
        response = self.client.post(self.BASE_URL, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('id') > 0)

    def test_post__large_name(self):
        data = {'name': 'Padaria de muitos caractereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees',
                'current_balance': 120000}
        with self.assertRaises(LargeNameException):
            self.client.post(self.BASE_URL, data)

    def test_post__required_fields(self):
        data1 = {'name': 'Padaria C'}
        data2 = {'current_balance': 18000}
        with self.assertRaises(RequiredValueException):
            self.client.post(self.BASE_URL, data1)
            self.client.post(self.BASE_URL, data2)




