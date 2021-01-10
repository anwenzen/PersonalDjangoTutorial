from django.contrib import admin

# Register your models here.

from blog.models import Message
from blog.models import Paper


class MessageModelsAdmin(admin.ModelAdmin):
    related_name = '留言'
    list_display = ('name', 'message', 'date_time')
    search_fields = ('name',)
    ordering = ('date_time',)