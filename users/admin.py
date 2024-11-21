from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile
from django.db import models
from django.conf import settings

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline,)
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("user", 'sex', 'home_university')
admin.site.register(Profile, AuthorAdmin)

# usr = User.objects.all()
# email = dir(usr[0])
# subject = 'welcome to GFG world'
# message = f'Hi {email} , thank you for being a stupid piece 0 shit.'
# email_from = settings.EMAIL_HOST_USER
# recip = 'artemoskin155@gmail.com'
# recipient_list = [recip, ]
# send_mail(subject, message, email_from, recipient_list)


