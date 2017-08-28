#!/usr/bin/env python
# -*- coding: utf-8 -*-
from payment.exceptions import PaymentNotFoundException, PaymentAlreadyPaidException
from payment.models import Payment


class PaymentService:

    def insert(self, request_data):
        payment = Payment()

        payment.expiration_date = request_data.get('expiration_date')
        payment.value = request_data.get('value')
        payment.branch_id = request_data.get('branch')

        payment.save()

        return Payment.objects.get(id=payment.id)

    def find_by_id(self, payment_id):
        return Payment.objects.filter(id=payment_id).first()

    def find(self, request_data):
        return Payment.objects.filter(**request_data).all()

    def update(self, payment_id, request_data):
        payment = Payment.objects.filter(id=payment_id).first()

        self.__validate(payment)

        expiration_date = request_data.get('expiration_date')
        value = request_data.get('value')
        branch = request_data.get('branch')

        update_fields = []
        if expiration_date:
            payment.expiration_date = expiration_date
            update_fields.append("expiration_date")

        if value:
            payment.value = value
            update_fields.append("value")

        if branch:
            payment.branch = branch
            update_fields.append("branch")

        payment.save(update_fields=update_fields)

        return Payment.objects.filter(id=payment_id).first()

    def delete(self, payment_id):
        payment = Payment.objects.filter(id=payment_id).first()

        self.__validate_exists(payment)

        payment.delete()

        return "Payment deleted successfully!"

    def __validate(self, payment):

        self.__validate_exists(payment)

        if payment.is_paid:
            raise PaymentAlreadyPaidException("Payment was already paid")

    def __validate_exists(self, payment):

        if not payment:
            raise PaymentNotFoundException("Payment not found!")


