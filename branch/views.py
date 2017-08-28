#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView

from branch.serializers import BranchSerializer
from branch.services import BranchService


class Branch(APIView):

    def __init__(self):
        self.service = BranchService()

    def post(self, request):
        """
        Record a new branch.
        ---
        parameters:
            - name: name
              description: Branch name. Maximum 100 characters.
              type: String
              paramType: query
              required: True
        """
        request_data = request.data
        data = self.service.insert(request_data)
        serializer = BranchSerializer(data)

        return Response(serializer.data)