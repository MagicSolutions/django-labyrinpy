from django.contrib import admin
from models import Message, Report


class MessageAdmin(admin.ModelAdmin):
    list_display = ('destination', 'message_type')
    search_fields = ('destination',)
    fieldsets = [
        (None, {'fields': ['destination', 'message_type']}),
        ('Optional Stuff', {'fields': [
                            'source_name',
                            'source',
                            'service',
                            'header',
                            'wap_text',
                            '_class',
                            'concatenate',
                            'unicode',
                            'validity',
                            'delivery',
                            'report'], 'classes': ['collapse']}),
    ]

admin.site.register(Message, MessageAdmin)
admin.site.register(Report)
