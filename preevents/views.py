from django.shortcuts import render
from .models import Event
from django.views.generic import DetailView

# Create your views here.
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events':events})
