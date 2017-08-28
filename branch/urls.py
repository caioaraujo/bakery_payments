#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from branch import views

urlpatterns = [
    url(r'^$', views.Branch.as_view()),
]