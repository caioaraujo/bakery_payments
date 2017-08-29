#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from branch.models import Branch as BranchModel
from branch.serializers import BranchSerializer, BranchResponseSerializer
from branch.services import BranchService


class Branch(GenericAPIView):
    serializer_class = BranchSerializer

    def __init__(self):
        self.service = BranchService()

    def post(self, request):
        """
        Record a new branch.
        """
        request_data = request.data
        data = self.service.insert(request_data)
        serializer = BranchResponseSerializer(data)

        return Response(serializer.data)

    def get_queryset(self):
        return BranchModel.objects.all()