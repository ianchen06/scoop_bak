from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from dal import autocomplete
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView

from webapp.forms import TaskForm, ConnectionForm
from webapp.models import Task, Connection
from webapp.tables import ConnectionTable, TaskTable
from webapp.filters import ConnectionFilter, TaskFilter

class FilteredTaskListView(SingleTableMixin, FilterView):
    table_class = TaskTable
    model = Task
    template_name = "webapp/task.html"

    filterset_class = TaskFilter

class FilteredConnectionListView(SingleTableMixin, FilterView):
    table_class = ConnectionTable
    model = Connection
    template_name = "webapp/connection.html"

    filterset_class = ConnectionFilter

class ConnectionListView(SingleTableView):
    model = Connection
    table_class = ConnectionTable
    template_name = 'webapp/connection.html'

class ConnectionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Task.objects.none()

        qs = Connection.objects.all()
        connection_type = self.forwarded.get('connection_type', None)

        if connection_type:
            qs = qs.filter(connection_type=connection_type)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

# Create your views here.
def home(request):
    context = {}
    return render(request, 'webapp/index.html', context)

def connection_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ConnectionForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_connection = form.save()
            return HttpResponseRedirect(reverse('connection'))
    else:
        form = ConnectionForm()
    return render(request, 'webapp/connection_create.html', {'form': form})

def task_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('home'))
    else:
        form = TaskForm()
    return render(request, 'webapp/task_create.html', {'form': form})
