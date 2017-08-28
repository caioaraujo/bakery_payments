#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class Branch(models.Model):
    """ Modelo da entidade Filial """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'branch'
