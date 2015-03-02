from django.contrib import admin
from sender.models import TwitterAccount

class TwitterAdmin(admin.ModelAdmin):
    list_display = ['name','active','id_twitter']

admin.site.register(TwitterAccount, TwitterAdmin)
