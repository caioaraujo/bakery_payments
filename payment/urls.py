#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from payment import views

urlpatterns = [
    url(r'^$', views.Payment.as_view()),
    url(r'^(?P<pk>\d+)$', views.PaymentId.as_view()),
]