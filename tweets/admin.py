from django.contrib import admin
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email']
    filter_fields = ['user']
    list_display = ['id', 'user' ]
    class Meta:
        model = Tweet


 
admin.site.register(Tweet, TweetAdmin)