from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from dal import autocomplete

from webapp.forms import TaskForm
from webapp.models import Task, Connection

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

def task(request):
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
    return render(request, 'webapp/task.html', {'form': form})
