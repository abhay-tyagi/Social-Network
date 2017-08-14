# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Like, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from .forms import Regform, PostForm
import datetime


def index(request):
    registration_form = Regform
    post_form = PostForm

    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'Website/index.html', {'posts': posts, 'post_form': post_form})

    return render(request, 'Website/index.html', {'reg_form': registration_form})


class register(View):
    form_class = Regform

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'Website/index.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        already_member = True

        if form.is_valid():
            user = form.save(commit=False)

            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)

            user.first_name = firstname
            user.last_name = lastname
            user.save()

            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('index')

        posts = Post.objects.all()
        return render(request, 'Website/index.html', {'already_member': already_member, 'posts': posts})


@method_decorator(login_required, name='dispatch')
class AddPost(View):
    form_class = PostForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'Website/index.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        already_member = True

        if form.is_valid():
            post = Post()
            post = form.save(commit=False)

            post.user = request.user
            post_content = form.cleaned_data['post_content']
            post.content = post_content
            post.time = datetime.datetime.now()
            post.date = datetime.date.today()
            post.save()

            return redirect('index')

        posts = Post.objects.all()
        return redirect('index')
        #return render(request, 'Website/index.html', {'already_member': already_member, 'posts': posts})


@login_required
def show_profile(request):
    return render(request, 'Website/show_profile.html')
