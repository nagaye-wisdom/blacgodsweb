from django.contrib import admin
# from .models import Member --- original
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(models.Member)


# class MemberPicInline(admin.StackedInline):
#     model = Member
#     can_delete = False
#
#
# class UserAdmin(UserAdmin):
#     inlines =[MemberPicInline]
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)