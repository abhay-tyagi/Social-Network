# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post


def index(request):
    all_posts = Post.objects.all();
    context = {
        "posts": all_posts
    }
    return render(request, 'Website/index.html', context)
