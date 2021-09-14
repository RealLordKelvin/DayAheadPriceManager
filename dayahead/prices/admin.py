from django.contrib import admin

# Register your models here.

from .models import Price, UserInfo

admin.site.register(Price)
admin.site.register(UserInfo)
