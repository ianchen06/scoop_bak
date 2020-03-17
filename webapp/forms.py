from django.forms import ModelForm, ModelChoiceField
from dal import autocomplete

from .models import Task, Connection

class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['connection'].widget.attrs = {
                'data-theme': 'bootstrap4',
                    }
    connection = ModelChoiceField(
            queryset=Connection.objects.all(),
            widget=autocomplete.ModelSelect2(url='connection-autocomplete', forward=['connection_type'])
            )

    class Meta:
        model = Task
        fields = ['name', 'connection_type', 'connection']
