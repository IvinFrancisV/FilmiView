from django.contrib import admin
from . models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(CustomUser, UserModel)
admin.site.register(Administrator)
admin.site.register(viewer)
admin.site.register(Trailer)
admin.site.register(Film)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Likes)
admin.site.register(Notifications)
admin.site.register(SubscriptionPlan)
admin.site.register(Subscription)
admin.site.register(Complaints)
admin.site.register(Userprofile)