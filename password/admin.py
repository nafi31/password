from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Website, Password
admin.site.unregister(Group)
admin.site.register(Website)
admin.site.register(Password)