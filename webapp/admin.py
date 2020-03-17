from django.contrib import admin

from webapp.models import Task, ConnectionType, Connection

# Register your models here.
admin.site.register(Task)
admin.site.register(Connection)
admin.site.register(ConnectionType)
