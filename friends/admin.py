from django.contrib import admin
from friends.models import Activity

class ActivityAdmin(admin.ModelAdmin):
    fields=['name','group','date']

admin.site.register(Activity,ActivityAdmin)