# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    temp_context = {
        "posts": "hello"
    }
    return render(request, 'Website/index.html', temp_context)
