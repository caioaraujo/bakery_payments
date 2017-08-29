#!/usr/bin/env python
# -*- coding: utf-8 -*-
from branch.exceptions import LargeNameException, RequiredValueException
from branch.models import Branch


class BranchService:

    def insert(self, request_data):
        branch = Branch()
        branch.name = request_data.get('name')
        branch.current_balance = request_data.get('current_balance')
        self.__validation(branch)

        branch.save()

        return Branch.objects.get(id=branch.id)

    def update_balance(self, branch_id, payment_value):
        """ Updates the branch balance for the given payment value """
        branch = Branch.objects.get(id=branch_id)
        branch.previous_balance = branch.current_balance
        branch.current_balance -= payment_value

        branch.save(update_fields=['current_balance', 'previous_balance'])

    def __validation(self, branch):

        if not branch.name:
            raise RequiredValueException("Name value is required")

        if not branch.current_balance:
            raise RequiredValueException("Current balance value is required")

        if len(branch.name) > 100:
            raise LargeNameException("Name must be lower than 100 chars")