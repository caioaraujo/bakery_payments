#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from branch.models import Branch


class BranchSerializer(serializers.ModelSerializer):
    """ Branch input data serializer """

    name = serializers.CharField(help_text="Branch name. Maximum 100 characters.", required=True)
    current_balance = serializers.FloatField(help_text="Branch's current balance.", required=True)

    class Meta:
        model = Branch
        fields = ('name', 'current_balance')


class BranchResponseSerializer(serializers.ModelSerializer):
    """ Custom branch response serializer """

    class Meta:
        model = Branch
        fields = ('id', 'name', 'current_balance', 'previous_balance')