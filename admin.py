from django.contrib import admin
from measure_snow.models import SnowSeason, SnowfallMeasure

class SnowfallMeasureAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'season', 'inches')
    list_filter = ['season', 'timestamp','inches']
    search_fields = ['inches']

admin.site.register(SnowSeason)
admin.site.register(SnowfallMeasure, SnowfallMeasureAdmin)
