from rest_framework import status
from rest_framework.test import APITestCase

from payment.exceptions import PaymentAlreadyPaidException, PaymentNotFoundException, BranchNotFoundException, \
    RequiredValueException


class PaymentTestsUsecase(APITestCase):
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
        result = response.data
        self.assertTrue(result.get('id') > 0)

    def test_post__branch_not_found(self):
        data = {'value': 12000, 'expiration_date': '2018-01-01', 'branch': 99}
        with self.assertRaises(BranchNotFoundException) as e:
            self.client.post(self.BASE_URL, data)
            self.assertEqual("Branch 99 not found in database", e.msg)

    def test_post__required_fields(self):
        data1 = {'value': 12000}
        data2 = {'expiration_date': '2018-01-01'}
        data3 = {'branch': 1}
        with self.assertRaises(RequiredValueException):
            self.client.post(self.BASE_URL, data1)
            self.client.post(self.BASE_URL, data2)
            self.client.post(self.BASE_URL, data3)

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
            self.client.put(self.BASE_URL + '2', data)

    def test_put__payment_not_found(self):
        data = {'value': 10000}
        with self.assertRaises(PaymentNotFoundException):
            self.client.put(self.BASE_URL + '99', data)

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


class PayTestsUsecase(APITestCase):
    fixtures = [
        'branch_fixtures',
        'payment_fixtures'
    ]

    def setUp(self):
        self.BASE_URL = '/payments/pay'

    # ==================================================================================================================
    # Post
    # ==================================================================================================================

    def test_post__success(self):
        data = {'payment': 1, 'date': '2015-02-01'}
        response = self.client.post(self.BASE_URL, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.data
        self.assertTrue(result.get('id') > 0)
        # Asserts branch balance
        self.assertEqual(130000.0, result.get('branch').get('previous_balance'))
        self.assertEqual((130000.0 - 13000.0), result.get('branch').get('current_balance'))

    def test_post__payment_not_found(self):
        data = {'payment': 99, 'date': '2015-02-01'}
        with self.assertRaises(PaymentNotFoundException):
            self.client.post(self.BASE_URL, data)

    def test_post__payment_date_required(self):
        data = {'payment': 1}
        with self.assertRaises(RequiredValueException):
            self.client.post(self.BASE_URL, data)

