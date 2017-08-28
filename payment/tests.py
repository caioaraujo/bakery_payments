from rest_framework import status
from rest_framework.test import APITestCase

from payment.exceptions import PaymentAlreadyPaidException, PaymentNotFoundException


class TestsUsecase(APITestCase):
    fixtures = [
        'branch_fixtures',
        'payment_fixtures'
    ]

    def setUp(self):
        self.BASE_URL = '/payments/'

    # ==================================================================================================================
    # Post
    # ==================================================================================================================

    def test_post__success(self):
        data = {'value': 12000, 'expiration_date': '2018-01-01', 'branch': 1}
        response = self.client.post(self.BASE_URL, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('id') > 0)

    # ==================================================================================================================
    # Put
    # ==================================================================================================================

    def test_put__success(self):
        data = {'value': 10000}
        response = self.client.put(self.BASE_URL + '1', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(10000, response.data.get('value'))

    def test_put__payment_was_paid(self):
        data = {'value': 10000}
        with self.assertRaises(PaymentAlreadyPaidException):
            response = self.client.put(self.BASE_URL + '2', data)

    def test_put__payment_not_found(self):
        data = {'value': 10000}
        with self.assertRaises(PaymentNotFoundException):
            response = self.client.put(self.BASE_URL + '99', data)

    # ==================================================================================================================
    # Delete
    # ==================================================================================================================

    def test_delete__success(self):
        response = self.client.delete(self.BASE_URL + '1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("Payment deleted successfully!", response.data)

    def test_delete__payment_not_found(self):
        with self.assertRaises(PaymentNotFoundException):
            self.client.delete(self.BASE_URL + '99')


