#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from branch.models import Branch


class BranchSerializer(serializers.ModelSerializer):

    name = serializers.CharField(help_text="Branch name. Maximum 100 characters.", required=True)

    class Meta:
        model = Branch
        fields = ('name',)


class BranchResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('id', 'name')