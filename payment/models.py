#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

from branch.models import Branch


class Payment(models.Model):
    """ Modelo da entidade Pagamento """
    id = models.AutoField(primary_key=True)
    value = models.FloatField()
    expiration_date = models.DateField()
    date_payment = models.DateField(null=True)
    branch = models.ForeignKey(Branch)
    is_paid = models.BooleanField(default=False)

    class Meta:
        db_table = 'payment'
