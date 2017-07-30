# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from Website.models import Profile, Post, Comment, Like

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
