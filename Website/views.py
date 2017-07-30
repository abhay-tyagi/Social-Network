# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Like, User
from django.contrib.auth import authenticate, login, logout

def index(request):
    
    return render(request, 'Website/index.html', {"posts": "hello"})
