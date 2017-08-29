#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import transaction

from branch.models import Branch
from branch.services import BranchService
from payment.exceptions import PaymentNotFoundException, PaymentAlreadyPaidException, RequiredValueException, \
    BranchNotFoundException
from payment.models import Payment


class PaymentService:

    def insert(self, request_data):
        """ Record a new payment """

        payment = Payment()

        payment.expiration_date = request_data.get('expiration_date')
        payment.value = request_data.get('value')
        payment.branch_id = request_data.get('branch')

        self.__validate_insert(payment)

        payment.save()

        return Payment.objects.get(id=payment.id)

    def find_by_id(self, payment_id):
        return Payment.objects.filter(id=payment_id).first()

    def find(self, request_data):
        return Payment.objects.filter(**request_data).all()

    def update(self, payment_id, request_data):
        payment = Payment.objects.filter(id=payment_id).first()

        self.__validate_update(payment)

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

    @transaction.atomic
    def do_pay(self, payment_id):
        """ Pay a payment and updates the branch balance """
        payment = Payment.objects.filter(id=payment_id).first()

        self.__validate_exists(payment)

        # Updates the branch balance before persist the payment
        self.__update_branch_balance(payment)

    def __update_branch_balance(self, payment):
        branch_service = BranchService()
        branch_service.update_balance(payment.branch_id, payment.value)

    def __validate_insert(self, payment):
        branch_id = payment.branch_id

        if not branch_id:
            raise RequiredValueException("Branch ID is required")

        if not payment.value:
            raise RequiredValueException("Payment value is required")

        if not payment.expiration_date:
            raise RequiredValueException("Expiration date value is required")

        # Validate the branch
        branch = Branch.objects.filter(id=branch_id).first()

        if not branch:
            raise BranchNotFoundException("Branch %s not found in database" % branch_id)

    def __validate_update(self, payment):

        self.__validate_exists(payment)

        if payment.is_paid:
            raise PaymentAlreadyPaidException("Payment was already paid")

    def __validate_exists(self, payment):

        if not payment:
            raise PaymentNotFoundException("Payment not found!")


