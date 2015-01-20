from django.contrib import admin

# Register your models here.
from project.apps.data import models

admin.site.register(models.MyUser)
admin.site.register(models.User_Profile)
admin.site.register(models.Question)
admin.site.register(models.Sector)
admin.site.register(models.Answer)
admin.site.register(models.Notification)