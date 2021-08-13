from django.contrib import admin
from .models import Query, WeekActivity

class QueryAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'protocol', 'debug',)
    list_display_links = ('datetime', 'protocol')
    search_fields = ('id', 'datetime',)
    list_filter = ('protocol', 'debug',)
    
    readonly_fields = tuple(field.name for field in Query._meta.fields)
        

class WeekActivityAdmin(admin.ModelAdmin):
    list_display = ('year', 'week', 'activity', 'protocol')
    list_display_links = ('year', 'week')
    search_fields = ('year', 'week',)
    list_filter = ('week', 'year', 'protocol')
    
    readonly_fields = tuple(field.name for field in WeekActivity._meta.fields)
    

admin.site.register(Query, QueryAdmin)
admin.site.register(WeekActivity, WeekActivityAdmin)