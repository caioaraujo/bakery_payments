#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from branch.models import Branch


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('id', 'name')