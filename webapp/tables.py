import django_tables2 as tables

from webapp.models import Connection

class ConnectionTable(tables.Table):
    class Meta:
        model = Connection
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "connection_type", "host", "port")
