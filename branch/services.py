#!/usr/bin/env python
# -*- coding: utf-8 -*-
from branch.exceptions import LargeNameException
from branch.models import Branch


class BranchService:

    def insert(self, request_data):
        branch = Branch()
        branch.name = request_data.get('name')
        self.__validation(branch)

        branch.save()

        return Branch.objects.get(id=branch.id)

    def __validation(self, branch):

        if len(branch.name) > 100:
            raise LargeNameException("Name must be lower than 100 chars")