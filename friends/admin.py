from django.contrib import admin
from friends.models import Activity, Profile


class ActivityAdmin(admin.ModelAdmin):
    fields=['name','group','date']

admin.site.register(Activity,ActivityAdmin)

admin.site.register(Profile)