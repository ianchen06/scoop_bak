import django_filters

from webapp.models import Connection

class ConnectionFilter(django_filters.FilterSet):
    class Meta:
        model = Connection
        fields = {"name": ["exact", "contains"], "connection_type": ["exact"]}
