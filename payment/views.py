#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from payment.filters import PaymentFilterBackend
from payment.serializers import PaymentSerializer, PaymentResponseSerializer
from payment.services import PaymentService


class Payment(GenericAPIView):
    serializer_class = PaymentSerializer
    filter_backends = (PaymentFilterBackend,)

    def __init__(self):
        self.service = PaymentService()

    def post(self, request):
        """
        Record a new payment.
        """
        request_data = request.data
        data = self.service.insert(request_data)
        serializer = PaymentResponseSerializer(data)

        return Response(serializer.data)

    def get(self, request):
        """
        Find payments by criteria.
        """
        request_path_params = request.GET.dict()
        data = self.service.find(request_path_params)

        serializer = PaymentResponseSerializer(data, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        pass

class PaymentId(GenericAPIView):
    serializer_class = PaymentSerializer

    def __init__(self):
        self.service = PaymentService()

    def get(self, request, **kwargs):
        """
        Find a specific payment by its ID.
        """
        payment_id = kwargs.get('pk')

        result = self.service.find_by_id(payment_id)
        serializer = PaymentResponseSerializer(result)

        return Response(serializer.data)

    def put(self, request, **kwargs):
        """
        Updates a payment information, if it was not paid yet
        """
        request_data = request.data
        payment_id = kwargs.get('pk')
        result = self.service.update(payment_id, request_data)
        serializer = PaymentResponseSerializer(result)

        return Response(serializer.data)

    def delete(self, request, **kwargs):
        """
        Delete a payment by its ID
        """
        payment_id = kwargs.get('pk')
        result = self.service.delete(payment_id)

        return Response(result)
