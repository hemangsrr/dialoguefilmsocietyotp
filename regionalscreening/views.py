from django.shortcuts import render
from .models import Screening
from django.views.generic import DetailView

# Create your views here.
def screening(request):
    screens = Screening.objects.all()
    return render(request, 'screening.html', {'screens':screens})
