import django_filters

from webapp.models import Connection, Task

class ConnectionFilter(django_filters.FilterSet):
    class Meta:
        model = Connection
        fields = {"name": ["exact", "contains"], "connection_type": ["exact"]}

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {"name": ["exact", "contains"], "connection_type": ["exact"]}
