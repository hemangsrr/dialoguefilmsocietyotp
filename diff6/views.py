from django.shortcuts import render
from django.views.generic import DetailView

# Create your views here.
def sample(request):
    return render(request, 'sample.html', {})
